from playwright.sync_api import Locator

from app.models.context import LocatorContext
from app.models.element import Element


class ParserService:
    """
    Parses the loaded webpage and converts interactive HTML
    elements into Element objects.
    """

    INTERACTIVE_TAGS = [
        "input",
        "button",
        "select",
        "textarea",
        "a"
    ]

    def parse(self, context: LocatorContext) -> LocatorContext:
        """
        Parse the page and populate context.elements.
        """

        page = context.page

        if page is None:
            raise RuntimeError("No page available in LocatorContext.")

        selector = ",".join(self.INTERACTIVE_TAGS)

        locator = page.locator(selector)

        count = locator.count()

        context.log(f"Found {count} interactive elements.")

        elements = []

        for index in range(count):

            node = locator.nth(index)

            try:
                element = self._build_element(node, index)

                elements.append(element)

            except Exception as e:
                context.log(
                    f"Failed to parse element {index}: {str(e)}"
                )

        context.elements = elements

        context.log(
            f"Successfully parsed {len(elements)} elements."
        )

        return context

    def classify_element(self, tag: str, input_type: str) -> str:

    if tag == "button":
        return "button"

    if tag == "select":
        return "dropdown"

    if tag == "textarea":
        return "textarea"

    if tag == "a":
        return "link"

    if tag == "input":

        mapping = {
            "text": "textbox",
            "email": "textbox",
            "password": "password",
            "checkbox": "checkbox",
            "radio": "radio",
            "submit": "button",
            "button": "button",
        }

        return mapping.get(input_type, "textbox")

    return tag

    def _build_element(
        self,
        node: Locator,
        index: int
    ) -> Element:
        """
        Convert a Playwright Locator into an Element object.
        """

        tag = node.evaluate(
            "el => el.tagName.toLowerCase()"
        )

        attributes = node.evaluate(
            """
            el => {
                const attrs = {};

                for (const attr of el.attributes){
                    attrs[attr.name] = attr.value;
                }

                return attrs;
            }
            """
        )

        try:
            text = node.inner_text().strip()
        except Exception:
            text = ""

        try:
            visible = node.is_visible()
        except Exception:
            visible = False

        try:
            enabled = node.is_enabled()
        except Exception:
            enabled = False

        label = ""

        element_id = attributes.get("id", "")
        element_type=self.classify_element(
            tag,
            attributes.get("type", "")
        )
        
        if element_id:

            try:

                page = node.page

                label_locator = page.locator(
                    f"label[for='{element_id}']"
                )

                if label_locator.count() > 0:

                    label = (
                        label_locator
                        .first
                        .inner_text()
                        .strip()
                    )

            except Exception:
                pass

        element = Element(

            index=index,

            tag=tag,

            text=text,

            id=attributes.get("id", ""),

            name=attributes.get("name", ""),

            type=attributes.get("type", ""),

            value=attributes.get("value", ""),

            placeholder=attributes.get(
                "placeholder",
                ""
            ),

            role=attributes.get(
                "role",
                ""
            ),

            href=attributes.get(
                "href",
                ""
            ),

            title=attributes.get(
                "title",
                ""
            ),

            aria_label=attributes.get(
                "aria-label",
                ""
            ),

            aria_role=attributes.get(
                "aria-role",
                ""
            ),

            data_testid=attributes.get(
                "data-testid",
                ""
            ),

            classes=attributes.get(
                "class",
                ""
            ).split(),

            attributes=attributes,

            visible=visible,

            enabled=enabled,

            label=label

        )
        
        return element
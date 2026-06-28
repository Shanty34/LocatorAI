class LocatorService:

    def generate(self, context):

        element = context.matched_element

        if element is None:
            return context

        locators = []

        attrs = element.attributes

        if "id" in attrs:
            locators.append(f"id={attrs['id']}")

        if "name" in attrs:
            locators.append(f"name={attrs['name']}")

        if "placeholder" in attrs:
            locators.append(
                f"xpath=//{element.tag}[@placeholder='{attrs['placeholder']}']"
            )

        if element.text:
            locators.append(
                f"xpath=//{element.tag}[normalize-space()='{element.text}']"
            )

        context.generated_locators = locators

        return context
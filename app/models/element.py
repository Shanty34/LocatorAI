from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Element:
    """
    Represents a single UI element extracted from the webpage.
    """

    # HTML Information
    tag: str
    text: str = ""

    # Common HTML attributes
    id: str = ""
    name: str = ""
    type: str = ""
    value: str = ""
    placeholder: str = ""
    role: str = ""
    href: str = ""
    title: str = ""
    element_type: str = ""
    # Accessibility
    aria_label: str = ""
    aria_role: str = ""

    # Test attributes
    data_testid: str = ""

    # CSS
    classes: List[str] = field(default_factory=list)

    # Raw attributes
    attributes: Dict[str, str] = field(default_factory=dict)

    # Generated locators
    xpath: str = ""
    css_selector: str = ""

    # Runtime properties
    visible: bool = True
    enabled: bool = True

    # Matching score
    score: int = 0

    def __str__(self) -> str:
        return (
            f"Element("
            f"tag={self.tag}, "
            f"text='{self.text}', "
            f"id='{self.id}', "
            f"name='{self.name}', "
            f"score={self.score})"
        )
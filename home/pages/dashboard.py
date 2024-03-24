"""The dashboard page."""

from home.templates import template
from home.state import StateChat

import reflex as rx

from home.components.chat import chat, action_bar


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Chat UI interface", size="8"),
        rx.text("Chat UI interface!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
        ),
        chat(),
        action_bar(),
        align="center",
    )

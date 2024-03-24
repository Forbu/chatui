import reflex as rx
from home import styles
from home.state import StateChat

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=styles.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=styles.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=StateChat.question,
            placeholder="Ask a question",
            on_change=StateChat.set_question,
            style=styles.input_style),
        rx.button("Ask", on_click=StateChat.answer, style=styles.button_style),
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            StateChat.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

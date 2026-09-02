import re
import textwrap

import streamlit as st

from config import STYLE_FILE


def inject_css():
    """Load and inject the dashboard stylesheet."""

    with open(
        STYLE_FILE,
        "r",
        encoding="utf-8",
    ) as f:

        css = f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )


def render_html(
    markup,
):
    """
    Safely render a multiline HTML fragment.

    Removes Python indentation and blank lines so that
    Streamlit's Markdown parser does not interpret nested
    HTML as a code block.
    """

    markup = textwrap.dedent(
        markup
    ).strip()

    markup = re.sub(
        r"\n[ \t]*\n",
        "\n",
        markup,
    )

    st.markdown(
        markup,
        unsafe_allow_html=True,
    )


def page_header(
    title,
    icon="",
    subtitle=None,
):

    render_html(
        f"""
        <div class="gv-header">
            <span class="gv-icon">{icon}</span>
            <h1 class="gv-title">{title}</h1>
        </div>
        """
    )

    if subtitle:

        st.markdown(
            f"""
            <p class="gv-subtitle">
                {subtitle}
            </p>
            """,
            unsafe_allow_html=True,
        )


def badge(
    text,
    tone="brass",
):

    return (
        f'<span class="gv-badge '
        f'gv-badge--{tone}">'
        f'{text}'
        f'</span>'
    )


def divider():

    st.markdown(
        '<hr class="gv-divider">',
        unsafe_allow_html=True,
    )


def section_card(
    title,
    caption=None,
):

    markup = f"""
    <div class="gv-card">
        <div class="gv-card-title">
            {title}
        </div>
    """

    if caption:

        markup += f"""
        <div class="gv-card-caption">
            {caption}
        </div>
        """

    markup += """
    </div>
    """

    render_html(markup)
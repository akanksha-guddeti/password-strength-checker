import streamlit as st
import re


# =========================================================
# PAGE SETTINGS
# =========================================================

st.markdown("""
<style>
.app-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    white-space: nowrap;
    color: #1e3a8a;
    margin-top: 20px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="app-title">🔐 PASSWORD STRENGTH CHECKER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center; font-size:18px; color:#64748b;">'
    'Check your password strength and improve your security.'
    '</p>',
    unsafe_allow_html=True
)



# =========================================================
# PASSWORD INPUT
# =========================================================

password = st.text_input(
    "🔑 Enter your password",
    type="password",
    placeholder="Enter password here..."
)


# =========================================================
# CHECK PASSWORD
# =========================================================

if password:

    # -----------------------------------------------------
    # SECURITY CHECKS
    # -----------------------------------------------------

    has_length = len(password) >= 8

    has_uppercase = bool(
        re.search(r"[A-Z]", password)
    )

    has_lowercase = bool(
        re.search(r"[a-z]", password)
    )

    has_number = bool(
        re.search(r"\d", password)
    )

    has_special = bool(
        re.search(r"[^A-Za-z0-9]", password)
    )


    # =====================================================
    # SCORE
    # =====================================================

    score = sum([
        has_length,
        has_uppercase,
        has_lowercase,
        has_number,
        has_special
    ])


    # =====================================================
    # PASSWORD STRENGTH
    # =====================================================

    st.subheader("📊 Password Strength")

    if score <= 2:

        st.error("🔴 Weak Password")

    elif score <= 4:

        st.warning("🟡 Medium Password")

    else:

        st.success("🟢 Strong Password")


    # =====================================================
    # SCORE
    # =====================================================

    st.metric(
        "Security Score",
        f"{score}/5"
    )

    st.progress(score / 5)


    # =====================================================
    # SECURITY REQUIREMENTS
    # =====================================================

    st.subheader("🛡️ Password Security")


    requirements = [
        ("🔤", "8+ characters", has_length),
        ("⬆️", "Uppercase letter", has_uppercase),
        ("🔡", "Lowercase letter", has_lowercase),
        ("🔢", "Number", has_number),
        ("✨", "Special character", has_special)
    ]


    # =====================================================
    # SHOW REQUIREMENTS
    # =====================================================

    for icon, requirement, passed in requirements:

        if passed:

            st.success(
                f"{icon} {requirement}   ✓ PASSED"
            )

        else:

            st.warning(
                f"{icon} {requirement}   ○ REQUIRED"
            )


    # =====================================================
    # SUGGESTIONS
    # =====================================================

    st.subheader("💡 Suggestions")


    suggestions = []


    if not has_length:
        suggestions.append(
            "Use at least 8 characters."
        )


    if not has_uppercase:
        suggestions.append(
            "Add an uppercase letter."
        )


    if not has_lowercase:
        suggestions.append(
            "Add a lowercase letter."
        )


    if not has_number:
        suggestions.append(
            "Add a number."
        )


    if not has_special:
        suggestions.append(
            "Add a special character like ! @ # $ %."
        )


    if suggestions:

        for suggestion in suggestions:

            st.info(
                f"💡 {suggestion}"
            )

    else:

        st.success(
            "🎉 Excellent! Your password meets all requirements."
        )


# =========================================================
# BEFORE ENTERING PASSWORD
# =========================================================

else:

    st.info(
        "🔎 Enter a password above to check its strength."
    )


# =========================================================
# SECURITY TIPS
# =========================================================

st.divider()

st.subheader("🔒 Quick Security Tips")

st.write("• Don't use your name or birthday.")
st.write("• Don't use common passwords.")
st.write("• Use a different password for important accounts.")
st.write("• Never share your password with anyone.")


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🔐 Password Strength Checker"
)
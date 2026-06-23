import random
import streamlit as st

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # #FIX: Start attempts at 0 to correct off-by-one in attempts left
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "feedback" not in st.session_state:
    st.session_state.feedback = []

if "celebrate" not in st.session_state:
    st.session_state.celebrate = False

st.subheader("Make a guess")

st.info(
    # #FIX: Use actual low/high range so main panel matches sidebar
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

# #FIX: Queue feedback in session_state so messages persist across reruns
for kind, text in st.session_state.feedback:
    getattr(st, kind)(text)
st.session_state.feedback = []

if st.session_state.celebrate:
    st.balloons()
    st.session_state.celebrate = False

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # #FIX: Reset all state and draw secret from difficulty range on new game
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.session_state.feedback.append(("error", err))
    else:
        st.session_state.history.append(guess_int)

        # #FIX: Compare against integer secret to remove string-cast glitch
        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.session_state.feedback.append(("warning", message))

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.session_state.celebrate = True
            st.session_state.status = "won"
            st.session_state.feedback.append((
                "success",
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}",
            ))
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.session_state.feedback.append((
                    "error",
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}",
                ))

    st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")

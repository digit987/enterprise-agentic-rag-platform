from app.db.postgres import SessionLocal

from app.models.conversation import Conversation


def save_conversation(
    session_id: str,
    user_query: str,
    assistant_response: str
):

    db = SessionLocal()

    conversation = Conversation(
        session_id=session_id,
        user_query=user_query,
        assistant_response=assistant_response
    )

    db.add(conversation)

    db.commit()

    db.close()


def get_conversation_history(
    session_id: str,
    limit: int = 5
):

    db = SessionLocal()

    conversations = (
        db.query(Conversation)

        .filter(
            Conversation.session_id == session_id
        )

        .order_by(
            Conversation.created_at.desc()
        )

        .limit(limit)

        .all()
    )

    db.close()

    history = []

    for conv in reversed(conversations):

        history.append({
            "user": conv.user_query,
            "assistant": conv.assistant_response
        })

    return history
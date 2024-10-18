async def send_email(subject, sender, recipients, text_body, html_body):
    """msg = Message(subject, recipients=recipients, sender=sender)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()"""
    print(text_body)

from scheduler.tasks import send_email_notification

if __name__ == "__main__":
    send_email_notification.delay()
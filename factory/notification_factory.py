from .notifications import EmailNotification, SMSNotification, PushNotification

class NotificationFactory:
    def create_notification(self, notification_type):
        notification_type = notification_type.lower()
        
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Неизвестный тип уведомления: {notification_type}")
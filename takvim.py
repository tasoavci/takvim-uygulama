from datetime import datetime

class User:
    def __init__(self, name, username, password, user_type):
        self.name = name
        self.username = username
        self.password = password
        self.user_type = user_type

class Event:
    def __init__(self, start_time, duration, event_type, description):
        self.start_time = start_time
        self.duration = duration
        self.event_type = event_type
        self.description = description

class CalendarApp:
    def __init__(self):
        self.users = []
        self.events = []

    def register_user(self):
        name = input("Adınız: ")
        username = input("Kullanıcı Adı: ")
        password = input("Şifre: ")
        user_type = input("Kullanıcı Tipi: ")
        user = User(name, username, password, user_type)
        self.users.append(user)
        print("Kullanıcı başarıyla kaydedildi!")
        self.show_user_menu(user)

    def create_event(self, user):
        start_time_input = input("Olayın Başlangıç Zamanı (GG.AA.YYYY HH:MM): ")
        start_time = datetime.strptime(start_time_input, "%d.%m.%Y %H:%M")
        duration = int(input("Olay Süresi (dakika): "))
        event_type = input("Olay Tipi: ")
        description = input("Olay Açıklaması: ")
        event = Event(start_time, duration, event_type, description)
        self.events.append((event, user))
        print("Olay başarıyla oluşturuldu!")
        self.show_user_menu(user)

    def view_user_events(self, user):
        user_events = [(event, u) for event, u in self.events if u.username == user.username]
        if len(user_events) == 0:
            print(f"{user.name} adlı kullanıcının olayları bulunamadı.")
        else:
            print(f"{user.name} adlı kullanıcının olayları:")
            for event, u in user_events:
                print("------------------------------")
                print(f"Olay: {event.event_type}")
                print(f"Başlangıç Zamanı: {event.start_time}")
                print(f"Süre: {event.duration} dakika")
                print(f"Açıklama: {event.description}")
            print("------------------------------")
        self.show_user_menu(user)


    def show_menu(self):
        print("\nAna Menü:")
        print("1. Kullanıcı Girişi")
        print("2. Çıkış")
        choice = input("Seçiminizi yapın (1-2): ")

        if choice == "1":
            self.register_user()
        elif choice == "2":
            print("Programdan çıkılıyor...")
        else:
            print("Geçersiz seçim. Tekrar deneyin.")
            self.show_menu()

    def show_user_menu(self, user):
        print("\nKullanıcı Menüsü:")
        print("1. Olayları Görüntüle")
        print("2. Olay Ekle")
        print("3. Ana Menü")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın (1-4): ")

        if choice == "1":
            self.view_user_events(user)
        elif choice == "2":
            self.create_event(user)
        elif choice == "3":
            self.show_menu()
        elif choice == "4":
            print("Programdan çıkılıyor...")
        else:
            print("Geçersiz seçim. Tekrar deneyin.")
            self.show_user_menu(user)

app = CalendarApp()
app.show_menu()

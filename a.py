import random

# Gheimat ha va tanzimat
gheymatVIP = 200000
gheymatREG = 150000
geymatECO = 100000
min_takhfif = 3
d_takhfif = 0.10


class Sans:
    def __init__(self, shenase, onvan, tarikh, radif, soton):
        self.shenase = str(shenase)  # Behtare string bashe baraye moghayese
        self.onvan = onvan
        self.tarikh_zaman = tarikh
        self.radif_ha = radif
        self.sotoon_ha = soton
        # Sakhtan matrix sandali ha (O = Khali, X = Por)
        self.sandaliha = [['O' for _ in range(soton)] for _ in range(radif)]
        self.tedad_kol_sandali = radif * soton
        self.tedad_rezerv_shode = 0

    def tedad_azad(self):
        return self.tedad_kol_sandali - self.tedad_rezerv_shode

    def namayesh_naghshe(self):
        print(f"\n--- Naghshe Salon: {self.onvan} ---")
        # Chap shomare sotoon ha
        header = "   "
        for i in range(self.sotoon_ha):
            header += f"{i + 1:2} "
        print(header)

        # Chap radif ha va vaziyat sandali
        for r in range(self.radif_ha):
            row_str = f"{r + 1:2} "
            for c in range(self.sotoon_ha):
                row_str += f"{self.sandaliha[r][c]:2} "
            print(row_str)
        print("-" * 30)

    def gheimat_sandali(self, radif):
        # Mohasebe gheimat bar asas jaye sandali
        if radif < self.radif_ha / 3:
            return gheymatVIP
        elif radif < (2 * self.radif_ha) / 3:
            return gheymatREG
        else:
            return geymatECO


class Rezerv:
    def __init__(self, idrezerv, username, idsans, list_sandali, price):
        self.shenase = str(idrezerv)
        self.nam_karbari = username
        self.shenase_sans = str(idsans)
        self.list_sandali = list_sandali  # Liste tuple ha (radif, sotoon)
        self.gheymat_kol = price


class SystemBilit:
    def __init__(self):
        self.users = {}  # {username: password}
        self.list_sans = []
        self.list_rezerv = []
        self.user_login = None
        self.add_sans_aye_avaliye()

    def add_sans_aye_avaliye(self):
        # Chand ta sans be onvan demo ezafe mikonim
        self.list_sans.append(Sans(101, "Film F1", "1404/12/01 - 18:00", 6, 8))
        self.list_sans.append(Sans(102, "Serial S26", "1404/12/06 - 20:00", 10, 10))
        self.list_sans.append(Sans(103, "Theater Soghot", "1404/12/05 - 19:30", 5, 6))

    def pause(self):
        input("\n>>> Baraye edame Enter bezanid...")

    def run(self):
        while True:
            self.show_menu()
            gozine = input("Entekhab: ")

            if gozine == '0':
                print("Khodahafex!")
                break
            elif gozine == '1':
                self.register()
            elif gozine == '2':
                self.login()
            elif gozine == '3':
                self.show_sans_ha()
                self.pause()
            elif gozine == '4':
                self.show_naghshe_sans()
                self.pause()
            elif gozine == '5':
                self.rezerv_kardan()
                self.pause()
            elif gozine == '6':
                self.show_my_rezerv()
                self.pause()
            elif gozine == '7':
                self.cancel_rezerv()
                self.pause()
            elif gozine == '8':
                self.edit_sandali()
                self.pause()
            elif gozine == '9':
                self.admin_report()
                self.pause()
            else:
                print("Gozine eshtebah ast.")

    def show_menu(self):
        who = self.user_login if self.user_login else "Mehman"
        print(f"\n=== Cinema Ticket System (User: {who}) ===")
        print("1. Sabt Nam")
        print("2. Vorood")
        print("3. List Sans ha")
        print("4. Didan Sandali ha")
        print("5. Rezerv Bilit")
        print("6. Rezerv haye Man")
        print("7. Laghv Rezerv")
        print("8. Taghir Sandali")
        print("9. Gozaresh (Admin)")
        print("0. Khoroj")
        print("================================")

    def register(self):
        u = input("Username: ")
        if u in self.users:
            print("In user ghablan bode!")
            return
        p = input("Password: ")
        self.users[u] = p
        print("Sabt nam shod. Hala login konid.")

    def login(self):
        u = input("Username: ")
        p = input("Password: ")
        if u in self.users and self.users[u] == p:
            self.user_login = u
            print(f"Salam {u}, vared shodid.")
        else:
            print("User ya Pass eshtebah ast.")

    def check_login(self):
        if self.user_login is None:
            print("Ebteda bayad vared shavid (Login).")
            return False
        return True

    def find_sans_by_id(self, sid):
        for s in self.list_sans:
            if s.shenase == str(sid):
                return s
        return None

    def show_sans_ha(self):
        print("\n--- Sans haye Mojood ---")
        for s in self.list_sans:
            print(f"ID: {s.shenase} | Film: {s.onvan} | Time: {s.tarikh_zaman} | Khali: {s.tedad_azad()}")

    def show_naghshe_sans(self):
        sid = input("ID Sans ro vared konid: ")
        s = self.find_sans_by_id(sid)
        if s:
            s.namayesh_naghshe()
        else:
            print("Sans peida nashod.")

    def rezerv_kardan(self):
        if not self.check_login(): return

        self.show_sans_ha()
        sid = input("Kodam ID ra mikhahid? ")
        sans = self.find_sans_by_id(sid)

        if sans is None:
            print("ID eshtebah ast.")
            return

        try:
            count = int(input("Chand ta bilit mikhahid? "))
        except:
            print("Lotfan adad bezanid.")
            return

        if count > sans.tedad_azad():
            print("Ja nist!")
            return

        sans.namayesh_naghshe()
        selected_seats = []
        total_price = 0

        print("Format vared kardan: Radif Fasele Sotoon (mesal: 2 5)")

        for i in range(count):
            ok = False
            while not ok:
                try:
                    inp = input(f"Sandali {i + 1}: ").split()
                    if len(inp) != 2:
                        print("Bayad 2 ta adad vared konid.")
                        continue

                    r = int(inp[0]) - 1
                    c = int(inp[1]) - 1

                    # Check mahdoode
                    if r < 0 or r >= sans.radif_ha or c < 0 or c >= sans.sotoon_ha:
                        print("In adad tooye naghshe nist.")
                        continue

                    # Check por boodan
                    if sans.sandaliha[r][c] == 'X':
                        print("Inja ghablan rezerv shode.")
                        continue

                    # Check tekrari too hamin rezerv
                    if (r, c) in selected_seats:
                        print("Ino hamin alan entekhab kardi.")
                        continue

                    selected_seats.append((r, c))
                    total_price += sans.gheimat_sandali(r)
                    ok = True
                except ValueError:
                    print("Adad vared konid!")

        # Mohasebe Takhfif
        if count >= min_takhfif:
            print(f"Shoma {int(d_takhfif * 100)}% takhfif gereftid!")
            total_price = int(total_price * (1 - d_takhfif))

        print(f"Mablagh Kol: {total_price} Toman")
        confirm = input("Taeed mikonid? (y/n): ")

        if confirm.lower() == 'y':
            # Sabt nahaee
            for r, c in selected_seats:
                sans.sandaliha[r][c] = 'X'
            sans.tedad_rezerv_shode += len(selected_seats)

            rid = random.randint(1000, 9999)
            new_res = Rezerv(rid, self.user_login, sans.shenase, selected_seats, total_price)
            self.list_rezerv.append(new_res)
            print(f"Anjam shod! Code Rezerv Shoma: {rid}")
        else:
            print("Cancel shod.")

    def show_my_rezerv(self):
        if not self.check_login(): return

        print(f"\n--- Rezerv haye {self.user_login} ---")
        found = False
        for r in self.list_rezerv:
            if r.nam_karbari == self.user_login:
                s = self.find_sans_by_id(r.shenase_sans)
                # Tabdil list tuple be string ghashang
                seats_str = ""
                for seat in r.list_sandali:
                    seats_str += f"({seat[0] + 1},{seat[1] + 1}) "

                print(f"Code: {r.shenase} | Film: {s.onvan} | Seats: {seats_str}| Pardakhti: {r.gheymat_kol}")
                found = True

        if not found:
            print("Hichi nist.")

    def cancel_rezerv(self):
        if not self.check_login(): return

        rid = input("Code Rezerv baraye laghv: ")
        target = None

        # Peida kardan rezerv
        for r in self.list_rezerv:
            if r.shenase == rid and r.nam_karbari == self.user_login:
                target = r
                break

        if target:
            sans = self.find_sans_by_id(target.shenase_sans)
            # Khali kardan sandali ha
            for r_idx, c_idx in target.list_sandali:
                sans.sandaliha[r_idx][c_idx] = 'O'

            sans.tedad_rezerv_shode -= len(target.list_sandali)
            self.list_rezerv.remove(target)
            print(f"Rezerv {rid} laghv shod va pool bargasht.")
        else:
            print("In code vojood nadarad ya mal shoma nist.")

    def edit_sandali(self):
        if not self.check_login(): return

        rid = input("Code Rezerv: ")
        target_res = None
        for r in self.list_rezerv:
            if r.shenase == rid and r.nam_karbari == self.user_login:
                target_res = r
                break

        if not target_res:
            print("Peyda nashod.")
            return

        sans = self.find_sans_by_id(target_res.shenase_sans)
        print(f"Sandali haye فعلی: {[(x + 1, y + 1) for x, y in target_res.list_sandali]}")

        # Gereftan voroodi baraye taghir
        try:
            print("Koodoom ro mikhahid avaz konid? (Radif Sotoon)")
            old_in = input("-> ").split()
            r_old, c_old = int(old_in[0]) - 1, int(old_in[1]) - 1

            if (r_old, c_old) not in target_res.list_sandali:
                print("In sandali too list shoma nist.")
                return

            sans.namayesh_naghshe()
            print("Jaye jadid kojast? (Radif Sotoon)")
            new_in = input("-> ").split()
            r_new, c_new = int(new_in[0]) - 1, int(new_in[1]) - 1

            # Check validity jadid
            if not (0 <= r_new < sans.radif_ha and 0 <= c_new < sans.sotoon_ha):
                print("Kharej az salon!")
                return
            if sans.sandaliha[r_new][c_new] == 'X':
                print("Onja pore.")
                return

            # Anjam taghirat
            # 1. Azad kardan ghadimi
            sans.sandaliha[r_old][c_old] = 'O'
            target_res.list_sandali.remove((r_old, c_old))

            # 2. Gereftan jadid
            sans.sandaliha[r_new][c_new] = 'X'
            target_res.list_sandali.append((r_new, c_new))

            # 3. Update gheimat (chon shayad az VIP be ECO bere ya baraks)
            new_total = 0
            for r, c in target_res.list_sandali:
                new_total += sans.gheimat_sandali(r)

            # Emal mojadad takhfif agar shamel beshe
            if len(target_res.list_sandali) >= min_takhfif:
                new_total = int(new_total * (1 - d_takhfif))

            target_res.gheymat_kol = new_total
            print(f"Sandali avaz shod. Gheimat jadid: {new_total}")

        except ValueError:
            print("Adad vared konid.")

    def admin_report(self):
        print("\n=== Gozaresh Modir ===")
        print(f"Total Rezervs: {len(self.list_rezerv)}")
        daramad = sum([r.gheymat_kol for r in self.list_rezerv])
        print(f"Total Daramad: {daramad}")

        for s in self.list_sans:
            print(f"> {s.onvan}: {s.tedad_azad()} ta khali az {s.tedad_kol_sandali}")


# Run barname
app = SystemBilit()
app.run()

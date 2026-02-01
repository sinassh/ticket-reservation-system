import random

gheymatVIP = 200000
gheymatREG = 150000
min_takhfif = 3
geymatECO = 100000
d_takhfif = 0.10

class Sans:
    def __init__(self, shenase, onvan, tarikh, radif_ha, sotoon_ha):
        self.shenase = shenase
        self.onvan = onvan
        self.tarikh_zaman = tarikh
        self.radif_ha = radif_ha
        self.sotoon_ha = sotoon_ha
        self.sandali_ha = [['O' for _ in range(sotoon_ha)] for _ in range(radif_ha)]
        self.kol_sandali_ha = radif_ha * sotoon_ha
        self.tedad_rezerv = 0

    def tedad_azad(self):
        return self.kol_sandali_ha - self.tedad_rezerv

    def namayesh_naghshe(self):
        print(f"\n--- Naqsh-e Sandali-ha-ye Sans: {self.onvan} ---")
        print("   " + " ".join([f"{i + 1:2}" for i in range(self.sotoon_ha)]))
        for radif in range(self.radif_ha):
            reshte_radif = " ".join([f"{self.sandali_ha[radif][sotoon]:2}" for sotoon in range(self.sotoon_ha)])
            print(f"{radif + 1:2} {reshte_radif}")
        print("-" * 20)

    def mohasebe_gheymat(self, radif):
        if radif < self.radif_ha / 3:
            return gheymatVIP
        elif radif < (2 * self.radif_ha) / 3:
            return gheymatREG
        else:
            return geymatECO

class Rezerv:
    def __init__(self, shenase_rezerv, nam_karbari, shenase_sans, sandali_ha, gheymat_kol):
        self.shenase = shenase_rezerv
        self.nam_karbari = nam_karbari
        self.shenase_sans = shenase_sans
        self.sandali_ha = sandali_ha
        self.gheymat_kol = gheymat_kol

class SystemBilit:
    def __init__(self):
        self.karbaran = {}
        self.sans_ha = []
        self.rezerv_ha = []
        self.karbar_jari = None
        self.rah_andazi_sans_ha()

    def rah_andazi_sans_ha(self):
        self.sans_ha.append(Sans(101, "film F1", "1404/12/01 - 18:00", 6, 8))
        self.sans_ha.append(Sans(102, "ronamye serie s26 ", "1404/12/06 - 20:00", 10, 10))
        self.sans_ha.append(Sans(103, "taatr soghot", "1404/12/05 - 19:30", 5, 6))

    def montazer_mandan(self):
        input("\n>>> lotfan baraye edame 'Enter' ra bezanid")

    def ejra(self):
        while True:
            self.chap_menu()
            entekhab = input("Entekhab konid: ")
            if entekhab == '0':
                print("Khoroj az barname!")
                break
            elif entekhab == '1':
                self.sabt_nam()
                self.montazer_mandan()
            elif entekhab == '2':
                self.vorood()
                self.montazer_mandan()
            elif entekhab == '3':
                self.namayesh_list_sans()
                self.montazer_mandan()
            elif entekhab == '4':
                self.namayesh_vaziyat_sans()
                self.montazer_mandan()
            elif entekhab == '5':
                self.rezerv_bilit()
                self.montazer_mandan()
            elif entekhab == '6':
                self.namayesh_rezerv_ha()
                self.montazer_mandan()
            elif entekhab == '7':
                self.laghv_rezerv()
                self.montazer_mandan()
            elif entekhab == '8':
                self.taghir_sandali()
                self.montazer_mandan()
            elif entekhab == '9':
                self.gozaresh_koli()
                self.montazer_mandan()
            else:
                print("Gozine-ye namotabar ast.")
                self.montazer_mandan()

    def chap_menu(self):
        vaziyat_karbar = f"(Karbar: {self.karbar_jari})" if self.karbar_jari else "(Mehman)"
        print(f"""\n=== System-e Rezerv-e Bilit {vaziyat_karbar} ===
        1. Sabt Nam
        2. Voroood
        3. Namayesh List Sans ha
        4. Namayesh Sandali ha Yek Sans
        5. Rezerv Bilit
        6. Namayesh Rezerv ha
        7. Laghv Rezerv
        8. Taghir Sandali
        9. Gozaresh Koli
        0. Khoroj
        $$$$$$$$$$$$$$$$$$$$""")

    def sabt_nam(self):
        nam_karbari = input("Nam-e Karbari Jadid: ")
        if nam_karbari in self.karbaran:
            print("Khatā: In nam-e karbari ghablan sabt shode ast.")
            return
        ramz_obour = input("Ramz-e Obour: ")
        self.karbaran[nam_karbari] = ramz_obour
        print("Sabat-nam ba movafaghiyat anjam shod.")

    def vorood(self):
        nam_karbari = input("Nam-e Karbari: ")
        ramz_obour = input("Ramz-e Obour: ")
        if nam_karbari in self.karbaran and self.karbaran[nam_karbari] == ramz_obour:
            self.karbar_jari = nam_karbari
            print(f"Khosh amadiid, {nam_karbari}!")
        else:
            print("Nam-e karbari ya ramz-e obour eshtebah ast.")

    def barresi_dastresi(self):
        if not self.karbar_jari:
            print("Khatā: Lotfan aval varod be hesab-e karbari shavid.")
            return False
        return True

    def namayesh_list_sans(self):
        print("\n--- List-e Sans-ha-ye Mojood ---")
        for sans in self.sans_ha:
            print(f"ID: {sans.shenase} | Unvan: {sans.onvan} | Zaman: {sans.tarikh_zaman} | Sandali-ye Azad: {sans.daryaft_tedad_azad()}")

    def peida_sans(self, shenase_sans):
        for sans in self.sans_ha:
            if str(sans.shenase) == str(shenase_sans):
                return sans
        return None

    def namayesh_vaziyat_sans(self):
        shenase_sans = input("Shenase-e Sans ra vared konid: ")
        sans = self.peida_sans(shenase_sans)
        if sans:
            sans.namayesh_naghshe()
        else:
            print("Sans yaft nashod.")

    def rezerv_bilit(self):
        if not self.barresi_dastresi(): return

        self.namayesh_list_sans()
        shenase_sans = input("Shenase-e Sans-e mored nazar baraye rezerv: ")
        sans = self.peida_sans(shenase_sans)
        if not sans:
            print("Sans namotabar.")
            return

        try:
            tedad = int(input("Tedad-e Sandali-e mored niyaz: "))
        except ValueError:
            print("Lotfan adad vared konid.")
            return

        if tedad <= 0:
            print("Tedad bayad bishtar az sifr bashad.")
            return

        if tedad > sans.daryaft_tedad_azad():
            print("Tedad-e sandali darkhasti bishtar az capacity baghimonde ast.")
            return

        sans.namayesh_naghshe()
        sandali_haye_entekhab_shode = []
        gheymat_movaghat = 0

        print("Rahnama: Shomare-ye Radef va Soton ra ba fasele vared konid (mesal: 1 2 baraye Radef 1, Soton 2)")

        for i in range(tedad):
            while True:
                try:
                    mokhtasat = input(f"Makhsasat-e Sandali {i + 1} (Radef Soton): ").split()
                    if len(mokhtasat) != 2: raise ValueError
                    radif, sotoon = int(mokhtasat[0]) - 1, int(mokhtasat[1]) - 1

                    if not (0 <= radif < sans.radif_ha and 0 <= sotoon < sans.sotoon_ha):
                        print("Sandali kharej az mahdoude ast.")
                        continue

                    if sans.sandali_ha[radif][sotoon] == 'X':
                        print("In Sandali ghablan rezerv shode ast.")
                        continue

                    if (radif, sotoon) in sandali_haye_entekhab_shode:
                        print("In Sandali ra ham-akhon entekhab kardid.")
                        continue

                    sandali_haye_entekhab_shode.append((radif, sotoon))
                    gheymat_movaghat += sans.mohasebe_gheymat(radif)
                    break

                except ValueError:
                    print("Format namotabar. Lotfan do adad vared konid.")

        if tedad >= min_takhfif:
            print(f"Shamel takhfif ({int(d_takhfif * 100)}%) shodid!")
            gheymat_movaghat = int(gheymat_movaghat * (1 - d_takhfif))

        print(f"Mablagh-e Ghabel-e Pardakht: {gheymat_movaghat} Toman")
        taeed = input("Aya taeed mikonid? (y/n): ")
        if taeed.lower() == 'y':
            for radif, sotoon in sandali_haye_entekhab_shode:
                sans.sandali_ha[radif][sotoon] = 'X'
            sans.tedad_rezerv += len(sandali_haye_entekhab_shode)

            shenase_rezerv = random.randint(1000, 9999)
            rezerv_jadid = Rezerv(shenase_rezerv, self.karbar_jari, sans.shenase, sandali_haye_entekhab_shode, gheymat_movaghat)
            self.rezerv_ha.append(rezerv_jadid)
            print(f"Rezerv ba movafaghiyat anjam shod. Code Rezerv: {shenase_rezerv}")
        else:
            print("Amaliyat laghv shod.")

    def namayesh_rezerv_ha(self):
        if not self.barresi_dastresi(): return

        print(f"\n--- Rezerv-ha-ye {self.karbar_jari} ---")
        peyda_shod = False
        for rezerv in self.rezerv_ha:
            if rezerv.nam_karbari == self.karbar_jari:
                peyda_shod = True
                sans = self.peida_sans(rezerv.shenase_sans)
                reshte_sandali = ", ".join([f"({radif + 1},{sotoon + 1})" for radif, sotoon in rezerv.sandali_ha])
                print(f"Code: {rezerv.shenase} | Film: {sans.onvan} | Sandali-ha: [{reshte_sandali}] | Mablagh: {rezerv.gheymat_kol}")

        if not peyda_shod:
            print("Hich rezervi yaft nashod.")

    def laghv_rezerv(self):
        if not self.barresi_dastresi(): return

        shenase_rezerv = input("Code Rezerv ra vared konid: ")

        rezerv_hadaf = None
        for rezerv in self.rezerv_ha:
            if str(rezerv.shenase) == shenase_rezerv and rezerv.nam_karbari == self.karbar_jari:
                rezerv_hadaf = rezerv
                break

        if not rezerv_hadaf:
            print("Rezerv yaft nashod ya motalegh be shoma nist.")
            return

        sans = self.peida_sans(rezerv_hadaf.shenase_sans)
        for radif, sotoon in rezerv_hadaf.sandali_ha:
            sans.sandali_ha[radif][sotoon] = 'O'
        sans.tedad_rezerv -= len(rezerv_hadaf.sandali_ha)

        self.rezerv_ha.remove(rezerv_hadaf)
        print("Rezerv laghv va mablagh bargasht dade shod.")

    def taghir_sandali(self):
        if not self.barresi_dastresi(): return

        shenase_rezerv = input("Code Rezerv ra vared konid: ")
        rezerv_hadaf = None
        for rezerv in self.rezerv_ha:
            if str(rezerv.shenase) == shenase_rezerv and rezerv.nam_karbari == self.karbar_jari:
                rezerv_hadaf = rezerv
                break

        if not rezerv_hadaf:
            print("Rezerv yaft nashod.")
            return

        sans = self.peida_sans(rezerv_hadaf.shenase_sans)
        print(f"Sandali-ha-ye fe'li: {[(radif + 1, sotoon + 1) for radif, sotoon in rezerv_hadaf.sandali_ha]}")

        try:
            mokhtasat_ghadimi = input("Kodam sandali ra mikhahid avaz konid? (Radef Soton): ").split()
            radif_ghadim, sotoon_ghadim = int(mokhtasat_ghadimi[0]) - 1, int(mokhtasat_ghadimi[1]) - 1

            if (radif_ghadim, sotoon_ghadim) not in rezerv_hadaf.sandali_ha:
                print("In sandali dar list rezerv shoma nist.")
                return

            sans.namayesh_naghshe()
            mokhtasat_jadid = input("Sandali jadid ra entekhab konid (Radef Soton): ").split()
            radif_jadid, sotoon_jadid = int(mokhtasat_jadid[0]) - 1, int(mokhtasat_jadid[1]) - 1

            if not (0 <= radif_jadid < sans.radif_ha and 0 <= sotoon_jadid < sans.sotoon_ha):
                print("Kharej az mahdoude.")
                return
            if sans.sandali_ha[radif_jadid][sotoon_jadid] == 'X':
                print("In sandali por ast.")
                return

            sans.sandali_ha[radif_ghadim][sotoon_ghadim] = 'O'
            rezerv_hadaf.sandali_ha.remove((radif_ghadim, sotoon_ghadim))

            sans.sandali_ha[radif_jadid][sotoon_jadid] = 'X'
            rezerv_hadaf.sandali_ha.append((radif_jadid, sotoon_jadid))

            gheymat_jadid_kol = 0
            for radif, sotoon in rezerv_hadaf.sandali_ha:
                gheymat_jadid_kol += sans.mohasebe_gheymat(radif)

            if len(rezerv_hadaf.sandali_ha) >= min_takhfif:
                gheymat_jadid_kol = int(gheymat_jadid_kol * (1 - d_takhfif))

            rezerv_hadaf.gheymat_kol = gheymat_jadid_kol
            print(f"Taghir anjam shod. Mablagh jadid: {gheymat_jadid_kol}")

        except ValueError:
            print("Vorodi namotabar.")

    def gozaresh_koli(self):
        print("\n=== Gozaresh Koli ===")
        daramad_kol = sum(rezerv.gheymat_kol for rezerv in self.rezerv_ha)
        print(f"Tedad Rezerv-ha: {len(self.rezerv_ha)}")
        print(f"Majmoo Foroush: {daramad_kol} Toman")
        for sans in self.sans_ha:
            print(f"- {sans.onvan}: {sans.daryaft_tedad_azad()} az {sans.kol_sandali_ha} azad")

if __name__ == "__main__":
    barname = SystemBilit()
    barname.ejra()
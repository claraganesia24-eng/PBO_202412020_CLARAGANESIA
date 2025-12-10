# Custom Exceptions
class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass


class UmurTerlaluMudaError(Exception):
    """Kesalahan jika umur kurang dari 5 tahun."""
    pass


class UmurTerlaluTuaError(Exception):
    """Kesalahan jika umur lebih dari 100 tahun."""
    pass


class AkunTidakDiizinkanError(Exception):
    """Kesalahan jika umur kurang dari 18 tahun untuk membuat akun."""
    pass


def set_umur(umur):
    """Validasi umur dasar + custom exception tambahan."""
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimal 100 tahun.")
    return umur


def daftar_akun(umur):
    """Validasi umur minimum 18 tahun untuk membuat akun."""
    if umur < 18:
        raise AkunTidakDiizinkanError("Umur kurang dari 18 tahun, tidak boleh membuat akun!")
    return True


if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)

            print("Umur valid:", umur)

            # Validasi pembuatan akun
            daftar_akun(umur)
            print("Akun berhasil dibuat!")

            break  # selesai jika semua valid

        except ValueError:
            print("Input harus berupa bilangan bulat!")
        except (UmurTidakValidError,
                UmurTerlaluMudaError,
                UmurTerlaluTuaError,
                AkunTidakDiizinkanError) as e:
            print("Error:", e)

        print("Silakan coba lagi.\n")

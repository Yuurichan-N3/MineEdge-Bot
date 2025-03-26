import requests
import time
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.logging import RichHandler
import logging

# Inisialisasi Rich Console
console = Console()

# Konfigurasi logging dengan RichHandler
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%Y-%m-%d %H:%M:%S]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger("MineEdgeBot")

# Banner
BANNER = """
╔══════════════════════════════════════════════╗
║       🌟 MineEdge Bot - Ad Reward Claim      ║
║   Automate your MineEdge ad reward claims!   ║
║  Developed by: https://t.me/sentineldiscus   ╚
╚══════════════════════════════════════════════╝
"""

# Fungsi untuk membaca initData dari file data.txt sebagai list akun
def read_init_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            return lines
    except FileNotFoundError:
        logger.error("File data.txt tidak ditemukan!")
        return None
    except Exception as e:
        logger.error(f"Error saat membaca file: {e}")
        return None

# Fungsi untuk mengirim request ke API
def claim_ad_reward(init_data, request_num, account_num):
    url = "https://mineedge.vercel.app/api/claimAdReward"
    
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://mineedge.vercel.app",
        "pragma": "no-cache",
        "referer": "https://mineedge.vercel.app/",
        "sec-ch-ua": '"Microsoft Edge";v="134", "Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge WebView2";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }

    payload = {
        "initData": init_data
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if response.status_code == 200 else "FAILED"
        message = "Ad reward claimed successfully!" if response.status_code == 200 else "Failed to claim ad reward"
        logger.info(f"Request #{request_num} (Akun #{account_num}) | Status: {status} | {message}")
        return response.status_code == 200
    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.error(f"Request #{request_num} (Akun #{account_num}) | Error: {e}")
        return False

def main():
    # Tampilkan banner
    console.print(BANNER, style="bold cyan")

    # Baca initData dari file
    file_path = "data.txt"
    init_data_list = read_init_data(file_path)
    if not init_data_list:
        console.print("[red]Tidak dapat melanjutkan tanpa initData. Pastikan data.txt ada dan berisi initData yang valid.[/red]")
        return

    # Tampilkan jumlah akun
    num_accounts = len(init_data_list)
    console.print(f"[green]Berhasil membaca data.txt ({num_accounts} akun)[/green]")

    # Input jumlah request dari pengguna
    while True:
        try:
            num_requests = int(console.input("[yellow]Masukkan jumlah request yang diinginkan: [/yellow]"))
            if num_requests <= 0:
                console.print("[red]Jumlah request harus lebih dari 0![/red]")
                continue
            break
        except ValueError:
            console.print("[red]Masukkan angka yang valid![/red]")

    # Tabel untuk ringkasan
    table = Table(title="Ringkasan Claim Ad Reward")
    table.add_column("Request #", style="cyan", no_wrap=True)
    table.add_column("Akun #", style="yellow", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Hasil", style="green")

    # Proses request
    success_count = 0
    for i in range(1, num_requests + 1):
        # Pilih akun berdasarkan index (looping jika request > jumlah akun)
        account_index = (i - 1) % num_accounts
        console.print(f"\n[bold blue]Memproses request #{i} untuk akun #{account_index + 1}...[/bold blue]")
        success = claim_ad_reward(init_data_list[account_index], i, account_index + 1)
        
        # Tambahkan ke tabel
        status = "Success" if success else "Failed"
        result = "Reward Claimed" if success else "Claim Failed"
        table.add_row(str(i), str(account_index + 1), status, result)
        
        if success:
            success_count += 1
        
        # Delay 3 detik antar request
        if i < num_requests:
            time.sleep(3)

    # Tampilkan ringkasan
    console.print(table)
    console.print(f"\n[bold green]Selesai! Total request: {num_requests} | Berhasil: {success_count} | Gagal: {num_requests - success_count}[/bold green]")

if __name__ == "__main__":
    main()

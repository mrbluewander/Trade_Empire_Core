import os
import platform
import socket
import time
from datetime import datetime

# ==========================================
# LOBSTER GENESIS - 萬象基地實戰驅動 v1.0
# 功能：同化環境偵測、探針掃描、自癒日誌
# ==========================================

class LobsterVanguard:
    def __init__(self):
        self.version = "1.0.0"
        self.log_file = "vanguard_healer.log"
        
    def get_env_data(self):
        """環境同化：抓取目前系統的物理特徵"""
        return {
            "OS": platform.system(),
            "OS_REL": platform.release(),
            "ARCH": platform.machine(),
            "TIME": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def network_probe(self):
        """網路探針：檢測通向外部資源的延遲與存取權"""
        targets = [("Google", "8.8.8.8"), ("GitHub", "140.82.112.3")]
        results = {}
        for name, ip in targets:
            start = time.time()
            try:
                # 建立極短暫的連線測試
                socket.create_connection((ip, 80), timeout=1)
                latency = (time.time() - start) * 1000
                results[name] = f"{latency:.2f}ms"
            except:
                results[name] = "BLOCKED"
        return results

    def write_heal_log(self, status_msg):
        """系統自癒日誌：記錄基地運作狀態"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [STATUS: {status_msg}]\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    def activate(self):
        print(f"--- 萬象基地 CORE v8.0 / SUCCESS_DEMO ---")
        env = self.get_env_data()
        print(f"[*] 環境偵測: {env['OS']} {env['OS_REL']} ({env['ARCH']})")
        
        print("[*] 啟動小龍蝦探針掃描...")
        net = self.network_probe()
        for target, res in net.items():
            print(f"    > {target}: {res}")
            
        self.write_heal_log("基地實體化任務成功執行")
        print(f"[*] [SUCCESS] 自癒日誌 {self.log_file} 已更新。")
        print(f"--- 任務序列結束 ---")

if __name__ == "__main__":
    vanguard = LobsterVanguard()
    vanguard.activate()

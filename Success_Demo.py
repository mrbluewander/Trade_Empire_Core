import os
import platform
import socket
import time
import subprocess
import json
from datetime import datetime

class LobsterVanguard:
    def __init__(self):
        self.status = "ACTIVE"
        self.log_file = "system_heal.log"
        self.birth_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def environment_scan(self):
        """全自動環境偵測：分析目前戰場規格"""
        info = {
            "os": platform.system(),
            "node": platform.node(),
            "cpu": platform.processor(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return info

    def network_latency_scan(self):
        """網路延遲掃描：檢測通向外部資源的滲透路徑"""
        targets = ["8.8.8.8", "github.com", "google.com"]
        results = {}
        for target in targets:
            start = time.time()
            try:
                socket.create_connection((target, 80), timeout=2)
                latency = (time.time() - start) * 1000
                results[target] = f"{latency:.2f}ms"
            except:
                results[target] = "TIMEOUT/BLOCKED"
        return results

    def self_healing_log(self, message):
        """系統自癒日誌：記錄每一次的同化與修補"""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] [SELF-HEAL] {message}\n")

    def run_mission(self):
        print("="*40)
        print(f"萬象基地 - 成功展示腳本 v1.0")
        print(f"激活時間: {self.birth_time}")
        print("="*40)
        
        # 1. 偵測環境
        env = self.environment_scan()
        print(f"> 環境偵測完成: {env['os']} ({env['node']})")
        
        # 2. 掃描網路
        print("> 啟動小龍蝦網路探針...")
        net = self.network_latency_scan()
        for t, l in net.items():
            print(f"  - 目標 {t}: {l}")
            
        # 3. 寫入日誌
        self.self_healing_log("基地展示任務成功執行。偵測到環境並完成網路通訊路徑確認。")
        print("\n> [SUCCESS] 自癒日誌已更新。基地實體化進度：15%")
        print("="*40)

if __name__ == "__main__":
    vanguard = LobsterVanguard()
    vanguard.run_mission()

import random

class TextLine:
    def __init__(self):
        self.initial_castles = [
            {'name': '姫路城', 'point': 8, 'defense': 7, 'owner': None, 'stability': 4, 'cycle': 0},
            {'name': '小田原城', 'point': 5, 'defense': 5, 'owner': None, 'stability': 5, 'cycle': 0},
            {'name': 'バッキンガム', 'point': 4, 'defense': 2, 'owner': None, 'stability': 2, 'cycle': 0},
            {'name': '甲子園', 'point': 5, 'defense': 3, 'owner': None, 'stability': 7, 'cycle': 0},
        ]

    def print_castle_status(self, castles):
        messages = ["\nキャッスルの現在の所有状況:"]
        for castle in castles:
            owner = castle['owner'] if castle['owner'] else "フリー"
            cycle_info = f"開発済{castle['cycle']}" if castle['cycle'] > 0 else ""
            messages.append(f"- {castle['name']}: ポイント {castle['point']}, 防御力 {castle['defense']}, 開発成功率 {castle['stability']},({owner} {cycle_info})")
        return messages

    def handle_victory(self, winner, castles):
        messages = [f"\n{winner}は、他の全てのキャッスルを開発しようとしている"]
        for castle in castles:
            previous_owner = castle['owner'] if castle['owner'] else "フリー"
            if previous_owner != winner:
                messages.append(f"'{castle['name']}'を{previous_owner}から奪取した！")
            castle['owner'] = winner
        for castle in castles:
            if castle['cycle'] == 0:
                messages.append(f"{winner}は'{castle['name']}'の開発に成功した！")
                castle['cycle'] = 2
        messages += self.print_castle_status(castles)
        return messages

    def process_player_cycles(self, castles, username, player_points):
        messages = []
        for castle in castles:
            if castle['cycle'] > 0 and castle['owner'] == username:
                castle['cycle'] -= 1
                messages.append(f"{username}の'{castle['name']}'の開発段階が1進んだ！")
                if castle['cycle'] == 0:
                    messages.append(f"'{castle['name']}'は{username}の開発を完了した！")
                    player_points += castle['point']
                    messages.append(f"{username}は現在{player_points}ポイント獲得！")
        return messages, player_points

    def process_cpu_cycles(self, castles, cpu_name, cpu_points):
        messages = []
        for castle in castles:
            if castle['cycle'] > 0 and castle['owner'] == cpu_name:
                castle['cycle'] -= 1
                messages.append(f"{cpu_name}の'{castle['name']}'の開発段階が1進んだ！")
                if castle['cycle'] == 0:
                    messages.append(f"'{castle['name']}'は{cpu_name}の開発を完了した！")
                    cpu_points += castle['point']
                    messages.append(f"{cpu_name}は現在{cpu_points}ポイント獲得！")
        return messages, cpu_points

    def player_turn(self, username, cpu_points, cpu2_points, player_points, castles):
        messages = [
            f"\n{username}は誰を攻撃/開発する？",
            f"CPUのポイント: {cpu_points}",
            f"CPU2のポイント: {cpu2_points}",
            f"{username}のポイント: {player_points}"
        ]
        messages += self.print_castle_status(castles)
        return messages

"""Resposta didática; não altera sistemas, acessos ou dispositivos."""

def recomendar_resposta(acesso_indevido):
    if acesso_indevido:
        return [
            "Isolar o sistema afetado",
            "Revogar acessos comprometidos",
            "Preservar registros para investigação",
        ]
    return ["Monitorar e verificar os fatos"]


if __name__ == "__main__":
    for medida in recomendar_resposta(True):
        print(medida)
    assert "Invadir dispositivo externo" not in recomendar_resposta(True)

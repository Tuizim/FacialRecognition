import os
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
TERMINAL_MESSAGE_MENU="""
═══════════════════════════════════════════════════════════════════
                ──── SYSTEM ACCESS CONTROL ────
═══════════════════════════════════════════════════════════════════
🚪  0. Fechar programa
   ────────────────────────────────

🛡️  1. Criar Usuário
   ────────────────────────────────
   Inicie o cadastro de um novo usuário com segurança.

🔍  2. Verificar Usuário
   ────────────────────────────────
   Consulte os dados de um usuário existente.


═══════════════════════════════════════════════════════════════════
🔔 Escolha uma opção digitando o número correspondente.
═══════════════════════════════════════════════════════════════════
"""
TERMINAL_MESSAGE_REGISTER="""
═══════════════════════════════════════════════════════════════════
                        ──── REGISTER ────
═══════════════════════════════════════════════════════════════════
"""
TERMINAL_MESSAGE_REGISTER_NAME="Nome: "
TERMINAL_MESSAGE_REGISTER_CPF="Cpf: "
TERMINAL_MESSAGE_REGISTER_STATUS="""
═══════════════════════════════════════════════════════════════════
                        ──── STATUS ────
═══════════════════════════════════════════════════════════════════
    1. Ativo
    0. Inativo
"""
TERMINAL_MESSAGE_VERIFY_FACE="""
═══════════════════════════════════════════════════════════════════
                        ──── VERIFICANDO FACE ────
═══════════════════════════════════════════════════════════════════
                Posicione seu rosto em frente da camera
"""

TERMINAL_MESSAGE_COMPLETED = """
═══════════════════════════════════════════════════════════════════
                    ────    CONCLUIDO    ────
═══════════════════════════════════════════════════════════════════
"""

TERMINAL_MESSAGE_TRY_AGAIN="""]
═══════════════════════════════════════════════════════════════════
                    ────    CONCLUIDO    ────
═══════════════════════════════════════════════════════════════════
Tecle algo para tentar novamente
"""
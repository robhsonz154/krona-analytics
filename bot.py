#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MENU PRINCIPAL - SIMULADORES SENAR
Curso Técnico em Agronegócio
Assessoria, Consultoria e Inovação no Agronegócio
"""

import subprocess
import sys
import os

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def exibir_menu():
    """Exibe o menu principal"""
    limpar_tela()
    print("="*60)
    print("   🌾 SIMULADORES SENAR - TÉCNICO EM AGRONEGÓCIO")
    print("   Assessoria, Consultoria e Inovação no Agronegócio")
    print("="*60)
    print()
    print("   Escolha o tema para simular a prova:")
    print()
    print("   [1] Tema 1 - Conceitos básicos de assessoria e consultoria")
    print("   [2] Tema 2 - Tendências e perspectivas para os serviços")
    print("   [3] Tema 3 - Modelo de negócios para prestadores de serviços")
    print("   [4] Tema 4 - Macro e microambiente dos negócios rurais")
    print("   [5] Tema 5 - Diagnóstico socioprodutivo, econômico e ambiental")
    print("   [6] Tema 6 - Papel dos serviços de consultoria para a inovação")
    print()
    print("   [0] Sair")
    print()
    print("-"*60)

def executar_simulador(tema):
    """Executa o script do simulador correspondente ao tema"""
    arquivo = f"simulador_tema{tema}.py"
    if not os.path.isfile(arquivo):
        print(f"\n❌ ERRO: Arquivo '{arquivo}' não encontrado na pasta atual!")
        input("\nPressione Enter para voltar ao menu...")
        return False
    
    print(f"\n🚀 Iniciando Simulador do Tema {tema}...\n")
    try:
        # Executa o script e aguarda término
        subprocess.run([sys.executable, arquivo])
    except Exception as e:
        print(f"\n❌ Erro ao executar: {e}")
    input("\n" + "="*60)
    input("Simulador finalizado. Pressione Enter para voltar ao menu...")
    return True

def main():
    while True:
        exibir_menu()
        opcao = input("   Digite sua opção: ").strip()
        
        if opcao == '0':
            print("\n👋 Saindo... Obrigado por estudar com o SENAR!\n")
            break
        elif opcao in ['1','2','3','4','5','6']:
            executar_simulador(int(opcao))
        else:
            print("\n⚠️ Opção inválida! Digite um número de 0 a 6.")
            input("\nPressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULADOR DE PREPARAÇÃO PARA PROVA - TEMA 4
Curso Técnico em Agronegócio (SENAR)
Módulo: Assessoria, Consultoria e Inovação no Agronegócio
Baseado fielmente no PDF (páginas 83 a 94)
"""

import random
import os

# Banco de questões do TEMA 4
questoes_tema4 = [
    # ===================== INTRODUÇÃO E CONCEITOS (p.84-86) =====================
    {
        "topico": "Conceitos de macro e microambiente",
        "subt": "Definição de macroambiente",
        "pergunta": "O macroambiente é composto por forças que afetam o microambiente e o nível interno das organizações. Sobre o macroambiente, é correto afirmar que:",
        "tipo": "mc",
        "opcoes": {
            "a": "As organizações têm total controle sobre as forças do macroambiente.",
            "b": "As forças do macroambiente afetam apenas um setor específico da economia.",
            "c": "As organizações não têm como controlar essas forças, precisando se adaptar e planejar sua atuação.",
            "d": "O macroambiente é composto apenas por fornecedores e clientes.",
            "e": "As forças macroambientais são as mesmas para todas as empresas, sem variações setoriais."
        },
        "correta": "c",
        "pagina": "85",
        "explicacao": "Página 85: 'Macroambiente: É composto por forças que afetam o microambiente e o nível interno das organizações, onde diferentes forças se combinam e atuam diretamente no comportamento delas, que não têm como controlar esse fenômeno. As organizações que quiserem se manter ativas vão precisar se adaptar e planejar sua atuação diante de tais forças.'"
    },
    {
        "topico": "Conceitos de macro e microambiente",
        "subt": "Definição de microambiente",
        "pergunta": "Sobre o microambiente, assinale a alternativa correta:",
        "tipo": "mc",
        "opcoes": {
            "a": "As organizações não têm qualquer controle sobre o microambiente.",
            "b": "É composto por forças mobilizadas por agentes e instituições mais diretamente ligadas à determinada empresa, sendo possível maior controle.",
            "c": "É o ambiente mais amplo, incluindo forças econômicas, políticas e tecnológicas.",
            "d": "Afeta igualmente todas as empresas de todos os setores.",
            "e": "É determinado exclusivamente pelo governo federal."
        },
        "correta": "b",
        "pagina": "85",
        "explicacao": "Página 85: 'Microambiente: É composto por forças mobilizadas por agentes e instituições mais diretamente ligadas à determinada empresa. O microambiente é mais específico e deve ser identificado em um segmento ou setor específico. É possível ter mais controle sobre os agentes, pois estão mais próximos.'"
    },

    # ===================== TÓPICO 1 - FORÇAS DO MACROAMBIENTE (p.86-89) =====================
    {
        "topico": "Análise do macroambiente dos negócios rurais",
        "subt": "Forças econômicas",
        "pergunta": "Dentre as cinco dimensões de força do macroambiente apresentadas no material (Chiavenato, 2014; Tavares, 2007), qual delas tem a capacidade de determinar o volume de operações, o nível de preços, a lucratividade e a facilidade de usar recursos básicos?",
        "tipo": "mc",
        "opcoes": {
            "a": "Forças políticas.",
            "b": "Forças tecnológicas.",
            "c": "Forças culturais.",
            "d": "Forças demográficas.",
            "e": "Forças econômicas."
        },
        "correta": "e",
        "pagina": "87",
        "explicacao": "Página 87: 'I. Forças econômicas: Esta força tem a capacidade de determinar o volume de operações, o nível de preços, lucratividade e facilidade ou dificuldade de usar os recursos básicos para os processos produtivos do negócio.'"
    },
    {
        "topico": "Macroambiente",
        "subt": "Forças políticas",
        "pergunta": "As forças políticas no macroambiente estão intimamente ligadas a:",
        "tipo": "mc",
        "opcoes": {
            "a": "Inovações tecnológicas e patentes.",
            "b": "Decisões dos governos municipais, estaduais e federais, incluindo leis tributárias e trabalhistas.",
            "c": "Características estatísticas da população, como idade e distribuição de renda.",
            "d": "Valores, hábitos e crenças da sociedade.",
            "e": "Taxas de câmbio e inflação."
        },
        "correta": "b",
        "pagina": "87",
        "explicacao": "Página 87: 'II. Forças políticas: Estão intimamente ligadas às decisões dos governos municipais, estaduais e federais. As tendências ideológicas podem influenciar... Estão relacionadas às leis (tributária e trabalhista, por exemplo), políticas educacionais e ambientais, entre outras.'"
    },
    {
        "topico": "Macroambiente",
        "subt": "Forças tecnológicas",
        "pergunta": "Para que as organizações se desenvolvam e sobrevivam no mercado competitivo, é necessário:",
        "tipo": "mc",
        "opcoes": {
            "a": "Ignorar as inovações tecnológicas para evitar riscos.",
            "b": "Acompanhar as inovações tecnológicas e incorporá-las aos seus processos produtivos.",
            "c": "Esperar que o governo forneça todas as tecnologias necessárias.",
            "d": "Utilizar apenas tecnologias ultrapassadas para reduzir custos.",
            "e": "Terceirizar toda a produção para empresas estrangeiras."
        },
        "correta": "b",
        "pagina": "87",
        "explicacao": "Página 87: 'III. Forças tecnológicas: Para que as organizações se desenvolvam e sobrevivam no mercado competitivo, é necessário acompanhar as inovações tecnológicas, e incorporá-las aos seus processos produtivos.'"
    },
    {
        "topico": "Macroambiente",
        "subt": "Forças culturais",
        "pergunta": "Verdadeiro ou Falso: As forças culturais estão ligadas aos valores, pressupostos básicos e hábitos da sociedade que influenciam as organizações, incluindo qualidade de vida no trabalho, diversidade e relações com comunidades tradicionais.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "88",
        "explicacao": "Página 88: 'IV. Forças culturais: Estão ligadas aos valores, pressupostos básicos e hábitos da sociedade que influenciam as organizações. Qualidade de vida no ambiente de trabalho, questões sobre diversidade, relações com comunidades tradicionais e suas crenças, mudanças nas preferências e nos interesses de consumo da população são pontos fundamentais.'"
    },
    {
        "topico": "Macroambiente",
        "subt": "Forças demográficas",
        "pergunta": "As forças demográficas representam características estatísticas da população. No Brasil, um fenômeno demográfico que mudará vários aspectos dos negócios é:",
        "tipo": "mc",
        "opcoes": {
            "a": "O aumento da natalidade.",
            "b": "O envelhecimento da população.",
            "c": "A redução da expectativa de vida.",
            "d": "O êxodo rural em massa.",
            "e": "A estabilização populacional."
        },
        "correta": "b",
        "pagina": "88",
        "explicacao": "Página 88: 'No Brasil, por exemplo, é cada vez mais evidente que o envelhecimento da população mudará vários aspectos relacionados aos comportamentos dos negócios.'"
    },

    # ===================== TÓPICO 2 - MICROAMBIENTE (p.89-92) =====================
    {
        "topico": "Análise do microambiente dos negócios rurais",
        "subt": "Definição de microambiente segundo Chiavenato",
        "pergunta": "Segundo Chiavenato (2014), o microambiente se refere:",
        "tipo": "mc",
        "opcoes": {
            "a": "Ao ambiente global que afeta todos os setores.",
            "b": "Ao local mais próximo e imediato da organização, constituindo o nicho onde ela desenvolve suas operações.",
            "c": "Apenas aos concorrentes diretos.",
            "d": "Às políticas governamentais de longo prazo.",
            "e": "Às condições climáticas e ambientais."
        },
        "correta": "b",
        "pagina": "90",
        "explicacao": "Página 90: 'O microambiente se refere ao local mais próximo e imediato da organização. Assim, cada uma tem o seu próprio e particular ambiente de tarefa que constitui o nicho onde ela desenvolve suas operações e de onde retira seus insumos e coloca seus produtos e serviços (CHIAVENATO, 2014).'"
    },
    {
        "topico": "Microambiente",
        "subt": "Agentes do microambiente",
        "pergunta": "Quais agentes fazem parte do microambiente da empresa, conforme o material?",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas os concorrentes.",
            "b": "Apenas os clientes.",
            "c": "Empresa, fornecedores, agências regulamentadoras, clientes, concorrentes, sindicatos, associações e cooperativas.",
            "d": "Somente o governo e as ONGs.",
            "e": "Apenas os acionistas e investidores."
        },
        "correta": "c",
        "pagina": "90",
        "explicacao": "Página 90: 'Portanto, o microambiente da empresa é constituído em um espaço onde há interação entre empresa, fornecedores, agências regulamentadoras ou de fiscalização, clientes, concorrentes, entre outros, como os sindicatos, associações e cooperativas.'"
    },
    {
        "topico": "Microambiente",
        "subt": "Produtor rural como tomador de preços",
        "pergunta": "No contexto do agronegócio, o produtor rural muitas vezes é um 'tomador de preços'. Isso significa que:",
        "tipo": "mc",
        "opcoes": {
            "a": "Ele define os preços dos seus produtos no mercado.",
            "b": "Ele aceita os preços determinados pelo mercado, sem poder influenciá-los significativamente.",
            "c": "Ele tem poder de barganha sobre todos os fornecedores.",
            "d": "Ele pode fixar preços acima do mercado.",
            "e": "Ele ignora os preços de mercado."
        },
        "correta": "b",
        "pagina": "90",
        "explicacao": "Página 90: 'O fato de o produtor ser um tomador de preços coloca seus fornecedores em uma posição confortável.' Ou seja, ele aceita os preços de mercado sem poder influenciá-los."
    },
    {
        "topico": "Microambiente",
        "subt": "Análise de risco",
        "pergunta": "O glossário do material define análise de risco como:",
        "tipo": "mc",
        "opcoes": {
            "a": "A eliminação completa de todas as incertezas do negócio.",
            "b": "Prever o futuro a partir do conhecimento do passado, exigindo conhecimento estatístico e grande banco de dados.",
            "c": "Aceitar todos os riscos sem qualquer planejamento.",
            "d": "Transferir todos os riscos para o governo.",
            "e": "Ignorar os riscos e focar apenas na produção."
        },
        "correta": "b",
        "pagina": "91",
        "explicacao": "Página 91 - Glossário: 'Análise de risco: compreende prever o futuro a partir do conhecimento do passado, o que exige conhecimento estatístico e grande banco de dados (LIMA, 2019).'"
    },

    # ===================== TÓPICO 3 - OPORTUNIDADES E AMEAÇAS (p.92-94) =====================
    {
        "topico": "Análise de oportunidades e ameaças de mercado",
        "subt": "Propósito da análise de cenários",
        "pergunta": "A análise de cenários no macro e microambiente tem como principal objetivo:",
        "tipo": "mc",
        "opcoes": {
            "a": "Eliminar completamente os concorrentes.",
            "b": "Encontrar oportunidades e ameaças para determinados negócios.",
            "c": "Reduzir o preço dos produtos a qualquer custo.",
            "d": "Aumentar a burocracia interna das empresas.",
            "e": "Substituir todos os gestores por consultores."
        },
        "correta": "b",
        "pagina": "92",
        "explicacao": "Página 92: 'Tais análises são feitas para encontrar oportunidades e ameaças para determinados negócios.'"
    },
    {
        "topico": "Oportunidades e ameaças",
        "subt": "Fatores externos a serem avaliados",
        "pergunta": "Para a análise do ambiente externo, deve-se avaliar, entre outros fatores:",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas a situação financeira da empresa.",
            "b": "Mudança de estratégias governamentais, taxas de câmbio, mudanças de hábitos do consumidor, surgimento de novos mercados e novas tecnologias.",
            "c": "Somente o clima e as condições do solo.",
            "d": "Apenas a rotatividade de funcionários.",
            "e": "Exclusivamente o fluxo de caixa."
        },
        "correta": "b",
        "pagina": "92",
        "explicacao": "Página 92: 'Para a análise do ambiente externo, deve-se avaliar, por exemplo, a mudança de estratégias governamentais, taxas de câmbio, mudanças de hábitos do consumidor, surgimentos de novos mercados, diversificação, entrada de novas tecnologias etc.'"
    },
    {
        "topico": "Oportunidades e ameaças",
        "subt": "Planejamento estratégico",
        "pergunta": "Uma das primeiras ações para se consolidar um modelo de gestão estratégica nas empresas rurais é:",
        "tipo": "mc",
        "opcoes": {
            "a": "Aumentar o número de funcionários.",
            "b": "Comprar mais terras.",
            "c": "Aplicar um planejamento estratégico.",
            "d": "Reduzir a produção pela metade.",
            "e": "Ignorar a concorrência."
        },
        "correta": "c",
        "pagina": "93",
        "explicacao": "Página 93: 'Uma das primeiras ações para se consolidar um modelo de gestão estratégica nas empresas rurais é a aplicação de um planejamento estratégico.'"
    },
    {
        "topico": "Oportunidades e ameaças",
        "subt": "Influência do ambiente externo no interno",
        "pergunta": "Verdadeiro ou Falso: O ambiente externo pode representar oportunidades ou ameaças ao desenvolvimento do planejamento estratégico, influenciando diretamente os fatores internos da organização.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "93",
        "explicacao": "Página 93: 'O ambiente externo pode representar oportunidades ou ameaças ao desenvolvimento do planejamento estratégico de qualquer organização. Por isso, a empresa deve estar atenta a ele, que influencia diretamente os fatores internos da organização.'"
    },
    {
        "topico": "Oportunidades e ameaças",
        "subt": "Sucesso da empresa rural",
        "pergunta": "De acordo com Santos et al. (2009), o sucesso da empresa rural dependerá do grau de:",
        "tipo": "mc",
        "opcoes": {
            "a": "Sorte e acaso nas negociações.",
            "b": "Gerenciamento estratégico do negócio, baseado em técnicas organizacionais e gerenciais de base científica.",
            "c": "Tamanho da propriedade em hectares.",
            "d": "Número de máquinas e implementos.",
            "e": "Tradição familiar na atividade."
        },
        "correta": "b",
        "pagina": "93",
        "explicacao": "Página 93: 'Assim, o sucesso da empresa rural dependerá do grau de gerenciamento estratégico do negócio, baseado em técnicas organizacionais e gerenciais de base científica (SANTOS et al., 2009).'"
    }
]

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_resultado(acertos, total):
    print("\n" + "="*70)
    print("   RESULTADO FINAL DO SIMULADOR (TEMA 4)")
    print("="*70)
    print(f"Total de questões: {total}")
    print(f"Acertos: {acertos}")
    print(f"Percentual: {acertos/total*100:.1f}%")
    if acertos/total >= 0.7:
        print("\n🎉 PARABÉNS! Você está preparado para a prova do TEMA 4.")
    elif acertos/total >= 0.5:
        print("\n📚 Bom desempenho! Revise os tópicos onde errou e tente novamente.")
    else:
        print("\n⚠️ Sugerimos revisar o material didático (páginas 83 a 94) antes da prova.")
    print("="*70)

def fazer_questao(q, num, total):
    print(f"\nQuestão {num} de {total}")
    print(f"Tópico: {q['topico']} | Subtópico: {q['subt']}")
    print("-"*70)
    print(q['pergunta'])
    print()
    if q['tipo'] == 'mc':
        for letra, texto in q['opcoes'].items():
            print(f"   {letra.upper()}) {texto}")
        print()
        while True:
            resp = input("Digite a letra da sua resposta (a, b, c, d, e): ").strip().lower()
            if resp in ['a','b','c','d','e']:
                break
            print("Opção inválida. Digite a, b, c, d ou e.")
        acertou = (resp == q['correta'])
        if acertou:
            print("\n✅ CORRETO!")
        else:
            print(f"\n❌ ERRADO. A alternativa correta é: {q['correta'].upper()}")
    else:  # verdadeiro/falso
        while True:
            resp = input("Digite V (Verdadeiro) ou F (Falso): ").strip().upper()
            if resp in ['V','F']:
                break
            print("Opção inválida. Digite V ou F.")
        acertou = (resp == q['correta'])
        if acertou:
            print("\n✅ CORRETO!")
        else:
            print(f"\n❌ ERRADO. A resposta correta é: {q['correta']}")
    print(f"\n📖 REFERÊNCIA (PDF): Página {q['pagina']}")
    print(f"📘 EXPLICAÇÃO: {q['explicacao']}")
    return acertou

def main():
    limpar_tela()
    print("="*70)
    print("   SIMULADOR DE PREPARAÇÃO PARA PROVA")
    print("   CURSO TÉCNICO EM AGRONEGÓCIO - SENAR")
    print("   MÓDULO: ASSESSORIA, CONSULTORIA E INOVAÇÃO")
    print("   TEMA 4: O MACRO E O MICROAMBIENTE DOS NEGÓCIOS RURAIS")
    print("="*70)
    print(f"\nEste simulador contém {len(questoes_tema4)} questões")
    print("cobrindo todos os tópicos do Tema 4 (páginas 83 a 94).")
    print("\nAs questões podem ser de múltipla escolha (A,B,C,D,E) ou Verdadeiro/Falso (V/F).")
    print("Ao final, você receberá seu percentual de acertos.\n")
    input("Pressione Enter para iniciar...")
    
    # Embaralhar questões
    questoes = random.sample(questoes_tema4, len(questoes_tema4))
    acertos = 0
    total = len(questoes)
    
    for i, q in enumerate(questoes, 1):
        limpar_tela()
        if fazer_questao(q, i, total):
            acertos += 1
        input("\nPressione Enter para a próxima questão...")
    
    limpar_tela()
    mostrar_resultado(acertos, total)

if __name__ == "__main__":
    main()
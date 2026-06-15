#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULADOR DE PREPARAÇÃO PARA PROVA - TEMA 5
Curso Técnico em Agronegócio (SENAR)
Módulo: Assessoria, Consultoria e Inovação no Agronegócio
Baseado fielmente no PDF (páginas 95 a 114)
"""

import random
import os

# Banco de questões do TEMA 5
questoes_tema5 = [
    # ===================== TÓPICO 1 - METODOLOGIA BÁSICA PARA CONSULTORIA GERENCIAL (p.97-102) =====================
    {
        "topico": "1. Metodologia básica para consultoria gerencial",
        "subt": "Etapas da metodologia",
        "pergunta": "Conforme o material, o ciclo básico de atuação da assessoria ou consultoria em uma empresa rural é composto por cinco etapas. Qual a sequência correta?",
        "tipo": "mc",
        "opcoes": {
            "a": "Implementação → Diagnóstico → Plano de ação → Análise externa → Avaliação.",
            "b": "Análise do ambiente externo → Análise do ambiente interno → Elaboração da análise SWOT → Plano de ações → Implementação e controle → Avaliação.",
            "c": "Plano de ação → Implementação → Diagnóstico → SWOT → Avaliação.",
            "d": "Avaliação → Implementação → Diagnóstico → Análise externa → Plano de ação.",
            "e": "Análise SWOT → Plano de ação → Implementação → Avaliação."
        },
        "correta": "b",
        "pagina": "97-101",
        "explicacao": "Páginas 97-101: as etapas são: a) Análise do ambiente externo (p.98), b) Análise do ambiente interno (p.99), c) Elaboração da análise Swot (p.100), d) Elaboração do plano de ações estratégicas (p.100), e) Implementação e controle do plano de ação (p.101), f) Avaliação dos resultados (p.101)."
    },
    {
        "topico": "1. Metodologia básica",
        "subt": "Análise do ambiente externo - macroambiente",
        "pergunta": "Na análise do ambiente externo da empresa rural, as forças macroambientais analisadas incluem: econômicas, políticas, tecnológicas, culturais e demográficas. Assinale a alternativa que apresenta corretamente uma análise do 'ambiente setorial' (antes e depois da porteira):",
        "tipo": "mc",
        "opcoes": {
            "a": "Forças econômicas e políticas.",
            "b": "Ameaças de entrada e permanência no mercado, poder de barganha de fornecedores e compradores, associações e cooperativas.",
            "c": "Taxas de câmbio e inflação.",
            "d": "Inovações tecnológicas e patentes.",
            "e": "Valores culturais e hábitos de consumo."
        },
        "correta": "b",
        "pagina": "98",
        "explicacao": "Página 98, quadro: Ambiente Setorial (Análise do antes e do depois da porteira) inclui: Ameaças de entrada e permanência no mercado, Intensidade de relação com parceiros/concorrentes, Pressão de produtos substitutos, Poder de barganha dos fornecedores/compradores, Associações e cooperativas, Câmaras Setoriais."
    },
    {
        "topico": "1. Metodologia básica",
        "subt": "Análise do ambiente interno",
        "pergunta": "Na análise do ambiente interno da empresa rural, qual das seguintes áreas NÃO é citada no material como uma das cinco áreas funcionais a serem analisadas?",
        "tipo": "mc",
        "opcoes": {
            "a": "Modelo de gestão e planejamento estratégico.",
            "b": "Gestão da produção.",
            "c": "Gestão de pessoas.",
            "d": "Gestão de marketing e comercialização.",
            "e": "Gestão de transporte e logística internacional."
        },
        "correta": "e",
        "pagina": "99",
        "explicacao": "Página 99, quadro: as áreas analisadas são: Modelo de gestão e planejamento estratégico, Gestão da produção, Gestão de pessoas, Gestão financeira e de custos, Gestão de marketing e comercialização. Não há 'Gestão de transporte e logística internacional' como uma área separada."
    },
    {
        "topico": "1. Metodologia básica",
        "subt": "Técnica 5W2H",
        "pergunta": "Qual dos itens a seguir NÃO é necessário considerar em um plano de ação desenvolvido com base na técnica 5W2H?",
        "tipo": "mc",
        "opcoes": {
            "a": "O que será feito?",
            "b": "Quanto vai custar cada ação?",
            "c": "Onde será aplicada cada ação?",
            "d": "Quando será executada cada ação?",
            "e": "Quantas linhas de crédito existem para cada ação?"
        },
        "correta": "e",
        "pagina": "102",
        "explicacao": "Página 102 (Atividade de aprendizagem 1): a resposta correta é 'Quantas linhas de crédito existem para cada ação?' pois não faz parte do 5W2H. O 5W2H inclui: What, Why, Where, When, Who, How, How much."
    },
    {
        "topico": "1. Metodologia básica",
        "subt": "Análise SWOT",
        "pergunta": "Qual é a técnica de análise do contexto empresarial que contribui para identificar forças, oportunidades, fraquezas e ameaças de um determinado negócio?",
        "tipo": "mc",
        "opcoes": {
            "a": "Método 5W2H.",
            "b": "Análise de concorrentes.",
            "c": "Análise Swot (ou Fofa).",
            "d": "Método de análise 'Entra e Sai'.",
            "e": "Benchmarking."
        },
        "correta": "c",
        "pagina": "102",
        "explicacao": "Página 102 (Atividade de aprendizagem 2): 'Análise Swot' é a técnica que identifica forças, oportunidades, fraquezas e ameaças."
    },
    {
        "topico": "1. Metodologia básica",
        "subt": "Plano de ação e criatividade",
        "pergunta": "Verdadeiro ou Falso: Os profissionais contratados pelas empresas rurais devem ser muito criativos e arrojados, capazes de propor ações inovadoras e de convencer o empresário rural de que é possível aplicá-las.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "101",
        "explicacao": "Página 101: 'Os profissionais contratados pelas empresas rurais devem ser muito criativos e arrojados, capazes de propor ações inovadoras e de convencer o empresário rural de que é possível aplicá-las.'"
    },

    # ===================== TÓPICO 2 - DIAGNÓSTICO RURAL PARTICIPATIVO (DRP) (p.103-107) =====================
    {
        "topico": "2. Metodologias de Diagnóstico Rural Participativo (DRP)",
        "subt": "Definição de DRP",
        "pergunta": "A partir do conteúdo estudado, marque a única alternativa que apresente corretamente a definição de Diagnóstico Rural Participativo.",
        "tipo": "mc",
        "opcoes": {
            "a": "O Diagnóstico Rural Participativo é um conjunto de técnicas e ferramentas que permite a obtenção direta de informação primária ou de campo, de modo que os atores sociais participam ativamente do processo.",
            "b": "O Diagnóstico Rural Participativo é uma técnica das empresas de assistência e extensão rural públicas, como a Emater.",
            "c": "O Diagnóstico Rural Participativo é um conjunto de técnicas aplicadas em grandes empresas rurais.",
            "d": "O Diagnóstico Rural Participativo é mais indicado para as agroindústrias, pois indica as melhores práticas de produção.",
            "e": "O Diagnóstico Rural Participativo é um conjunto de técnicas e ferramentas para a formulação de ações governamentais."
        },
        "correta": "a",
        "pagina": "107",
        "explicacao": "Página 107 (Atividade de aprendizagem 1): a definição correta é a alternativa A, conforme Drumond et al (2009) e Chambers (1982)."
    },
    {
        "topico": "2. DRP",
        "subt": "Origem e definição segundo Chambers",
        "pergunta": "Chambers (1982) definiu o Diagnóstico Rural Participativo como:",
        "tipo": "mc",
        "opcoes": {
            "a": "Um método exclusivo para grandes propriedades.",
            "b": "Um conjunto de métodos e abordagens que possibilitam às comunidades compartilhar e analisar sua percepção acerca de suas condições de vida, planejar e agir.",
            "c": "Uma técnica de fiscalização governamental.",
            "d": "Um sistema de certificação de produtos orgânicos.",
            "e": "Um método de precificação de consultoria."
        },
        "correta": "b",
        "pagina": "104",
        "explicacao": "Página 104: 'Chambers (1982) definiu o Diagnóstico Rural Participativo (DRP) como uma metodologia estrategicamente pensada para determinar “um conjunto de métodos e abordagens que possibilitam às comunidades compartilhar e analisar sua percepção acerca de suas condições de vida, planejar e agir”.'"
    },
    {
        "topico": "2. DRP",
        "subt": "Exemplos de técnicas do DRP",
        "pergunta": "O material cita que o DRP utiliza técnicas que permitem maior visualização e compartilhamento das informações. Assinale a alternativa que apresenta exemplos dessas técnicas:",
        "tipo": "mc",
        "opcoes": {
            "a": "Questionários fechados e entrevistas individuais.",
            "b": "Confecção de mapas, diagramas e rankings.",
            "c": "Apenas observação participante.",
            "d": "Análise de laboratório e amostragem de solo.",
            "e": "Levantamento topográfico e georreferenciamento."
        },
        "correta": "b",
        "pagina": "105",
        "explicacao": "Página 105: 'Uso de técnicas que permitem maior visualização e compartilhamento das informações. Citam-se como exemplo a confecção de mapas, diagramas e rankings.'"
    },
    {
        "topico": "2. DRP",
        "subt": "Pesquisa-ação",
        "pergunta": "A principal característica de pesquisa para quem trabalha com DRP é a pesquisa-ação. Sobre ela, o material afirma que:",
        "tipo": "mc",
        "opcoes": {
            "a": "É uma técnica que dispensa o contato com os agricultores.",
            "b": "É uma técnica de pesquisa estratégica que fornece subsídios para a melhoria de processos e tomada de decisões.",
            "c": "É um método exclusivo de análise estatística.",
            "d": "É uma ferramenta de fiscalização ambiental.",
            "e": "É um sistema de credenciamento de consultores."
        },
        "correta": "b",
        "pagina": "106",
        "explicacao": "Página 106: 'A pesquisa-ação é uma técnica de pesquisa estratégica a qual os técnicos em agronegócio podem recorrer para melhorarem o processo de produção e comercialização... O benefício da pesquisa-ação está em fornecer subsídios para a melhoria de processos que orientem as mudanças necessárias para melhorar a tomada de decisões.'"
    },
    {
        "topico": "2. DRP",
        "subt": "Ferramenta 'Entra e Sai'",
        "pergunta": "A ferramenta 'Entra e Sai' apresentada no material é utilizada para:",
        "tipo": "mc",
        "opcoes": {
            "a": "Analisar os fluxos de custos (Entra) e receitas (Sai) na propriedade rural.",
            "b": "Controlar a entrada e saída de pessoas na fazenda.",
            "c": "Gerenciar o estoque de insumos.",
            "d": "Calcular o ponto de equilíbrio financeiro.",
            "e": "Elaborar contratos de consultoria."
        },
        "correta": "a",
        "pagina": "106-107",
        "explicacao": "Página 106-107: a ferramenta 'Entra e Sai' mostra um esquema onde 'Antes da Porteira' entram custos (calcário, adubação, sementes, máquinas, ração, medicamentos), 'Dentro da Porteira' ocorre o processo produtivo (grãos, galinhas, peixes), e 'Depois da Porteira' saem as receitas (ovos, carnes)."
    },

    # ===================== TÓPICO 3 - METODOLOGIA ATEG/SENAR (p.108-114) =====================
    {
        "topico": "3. Metodologia Assistência Técnica e Gerencial do SENAR (ATeG)",
        "subt": "Início do programa",
        "pergunta": "O programa de Assistência Técnica e Gerencial (ATeG) do SENAR foi iniciado em qual ano?",
        "tipo": "mc",
        "opcoes": {
            "a": "2010.",
            "b": "2016.",
            "c": "2018.",
            "d": "2020.",
            "e": "2008."
        },
        "correta": "b",
        "pagina": "108",
        "explicacao": "Página 108: 'O Serviço Nacional de Aprendizagem Rural (SENAR), iniciou o programa de Assistência Técnica e Gerencial (ATeG) no ano de 2016.'"
    },
    {
        "topico": "3. ATeG/SENAR",
        "subt": "Extinção da Embrater",
        "pergunta": "O material menciona que a extinção da Embrater (Empresa Brasileira de Assistência Técnica e Extensão Rural) ocorreu em que ano, concentrando o conhecimento entre grandes produtores?",
        "tipo": "mc",
        "opcoes": {
            "a": "1985.",
            "b": "1990.",
            "c": "1995.",
            "d": "2000.",
            "e": "2005."
        },
        "correta": "b",
        "pagina": "109",
        "explicacao": "Página 109: 'A extinção da Embrater... em 1990, concentrou o conhecimento entre os grandes produtores rurais em detrimento dos médios e pequenos.'"
    },
    {
        "topico": "3. ATeG/SENAR",
        "subt": "Diferencial da metodologia",
        "pergunta": "Qual é o principal diferencial da metodologia ATeG/SENAR?",
        "tipo": "mc",
        "opcoes": {
            "a": "Nela, os produtores têm acesso a um modelo único de assessoria, pois as dimensões gerenciais e organizacionais das propriedades rurais são devidamente analisadas, e não somente as questões relacionadas aos sistemas produtivos de forma isolada.",
            "b": "O maior diferencial da ATeG/SENAR é o acompanhamento contínuo do negócio rural por mais de 4 anos.",
            "c": "O grande diferencial da ATeG/SENAR é o foco nas questões relacionadas às melhores práticas de produção agropecuária.",
            "d": "O grande diferencial da metodologia ATeG/SENAR é o foco na coordenação e na gestão de pessoas das principais cadeias produtivas do país.",
            "e": "A metodologia tem foco na gestão dos custos totais dos sistemas de produção das empresas rurais da cadeia produtiva da bovinocultura de leite."
        },
        "correta": "a",
        "pagina": "113",
        "explicacao": "Página 113 (Atividade de aprendizagem 1): 'Nela, os produtores têm acesso a um modelo único de assessoria, pois as dimensões gerenciais e organizacionais das propriedades rurais são devidamente analisadas, e não somente as questões relacionadas aos sistemas produtivos de forma isolada.'"
    },
    {
        "topico": "3. ATeG/SENAR",
        "subt": "Objetivos do programa",
        "pergunta": "Qual dos itens a seguir NÃO pode ser apontado como um dos objetivos da ATeG/SENAR?",
        "tipo": "mc",
        "opcoes": {
            "a": "Capacitar o produtor rural para o empreendedorismo e a gestão do negócio.",
            "b": "Elevar a renda e a produtividade da propriedade rural por meio do aumento da eficiência e da eficácia.",
            "c": "Aumentar a rentabilidade dos negócios rurais.",
            "d": "Estabelecer o perfil e o comportamento dos consumidores finais das cadeias produtivas do agronegócio.",
            "e": "Elaborar o planejamento estratégico da propriedade rural."
        },
        "correta": "d",
        "pagina": "113",
        "explicacao": "Página 113 (Atividade de aprendizagem 2): 'Estabelecer o perfil e o comportamento dos consumidores finais' não é um objetivo da ATeG/SENAR. Os objetivos são: capacitar o produtor, elevar renda/produtividade, aumentar rentabilidade, estabelecer perfil tecnológico/social/econômico, elaborar planejamento estratégico."
    },
    {
        "topico": "3. ATeG/SENAR",
        "subt": "Etapas da metodologia",
        "pergunta": "A metodologia de Assistência Técnica e Gerencial do SENAR está fundamentada em cinco etapas. Assinale a alternativa que apresenta a sequência correta:",
        "tipo": "mc",
        "opcoes": {
            "a": "Planejamento estratégico → Diagnóstico → Adequação tecnológica → Capacitação → Avaliação.",
            "b": "Diagnóstico produtivo individualizado → Planejamento estratégico → Adequação tecnológica → Capacitação profissional complementar → Avaliação sistemática de resultados.",
            "c": "Adequação tecnológica → Diagnóstico → Planejamento → Capacitação → Avaliação.",
            "d": "Capacitação → Diagnóstico → Planejamento → Adequação → Avaliação.",
            "e": "Avaliação → Capacitação → Adequação → Planejamento → Diagnóstico."
        },
        "correta": "b",
        "pagina": "110",
        "explicacao": "Página 110: as cinco etapas são: 1º Diagnóstico produtivo individualizado; 2º Planejamento estratégico; 3º Adequação tecnológica; 4º Capacitação profissional complementar; 5º Avaliação sistemática de resultados."
    },
    {
        "topico": "3. ATeG/SENAR",
        "subt": "Limite de atendimento por técnico",
        "pergunta": "De acordo com o material, cada técnico do programa ATeG pode atender até quantos produtores?",
        "tipo": "mc",
        "opcoes": {
            "a": "10 produtores.",
            "b": "20 produtores.",
            "c": "30 produtores.",
            "d": "40 produtores.",
            "e": "50 produtores."
        },
        "correta": "c",
        "pagina": "111",
        "explicacao": "Página 111: 'Os grupos atendidos pela equipe do SENAR são limitados. Cada técnico pode atender até 30 produtores.'"
    },
    {
        "topico": "3. ATeG/SENAR",
        "subt": "Público-alvo da ATeG",
        "pergunta": "A metodologia ATeG/SENAR foi criada para auxiliar principalmente os produtores rurais de quais classes?",
        "tipo": "mc",
        "opcoes": {
            "a": "Classes A e B (alta renda).",
            "b": "Classes C, D e que não têm acesso à extensão rural e às novas tecnologias.",
            "c": "Apenas agricultores familiares do Nordeste.",
            "d": "Grandes agroindústrias exportadoras.",
            "e": "Produtores de soja e milho do Centro-Oeste."
        },
        "correta": "b",
        "pagina": "109",
        "explicacao": "Página 109: 'o SENAR criou a Metodologia de Assistência Técnica e Gerencial para auxiliar, principalmente, os produtores rurais das classes C, D e que não têm acesso à extensão rural e às novas tecnologias.'"
    },
    {
        "topico": "3. ATeG/SENAR",
        "subt": "Dados do Censo Agropecuário sobre classes de renda",
        "pergunta": "Segundo dados do Censo Agropecuário apresentados no material, qual classe de renda rural tem o maior contingente de estabelecimentos (aproximadamente 3,6 milhões)?",
        "tipo": "mc",
        "opcoes": {
            "a": "Classe A/B.",
            "b": "Classe C.",
            "c": "Classe D/E.",
            "d": "Classe B.",
            "e": "Classe A."
        },
        "correta": "c",
        "pagina": "109",
        "explicacao": "Página 109: 'A classe D/E tem o maior contingente, com 3,6 milhões de estabelecimentos (70,4% do número total).'"
    }
]

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_resultado(acertos, total):
    print("\n" + "="*70)
    print("   RESULTADO FINAL DO SIMULADOR (TEMA 5)")
    print("="*70)
    print(f"Total de questões: {total}")
    print(f"Acertos: {acertos}")
    print(f"Percentual: {acertos/total*100:.1f}%")
    if acertos/total >= 0.7:
        print("\n🎉 PARABÉNS! Você está preparado para a prova do TEMA 5.")
    elif acertos/total >= 0.5:
        print("\n📚 Bom desempenho! Revise os tópicos onde errou e tente novamente.")
    else:
        print("\n⚠️ Sugerimos revisar o material didático (páginas 95 a 114) antes da prova.")
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
    print("   TEMA 5: DIAGNÓSTICO SOCIOPRODUTIVO, ECONÔMICO")
    print("          E AMBIENTAL DOS NEGÓCIOS RURAIS")
    print("="*70)
    print(f"\nEste simulador contém {len(questoes_tema5)} questões")
    print("cobrindo todos os tópicos do Tema 5 (páginas 95 a 114).")
    print("\nAs questões podem ser de múltipla escolha (A,B,C,D,E) ou Verdadeiro/Falso (V/F).")
    print("Ao final, você receberá seu percentual de acertos.\n")
    input("Pressione Enter para iniciar...")
    
    # Embaralhar questões
    questoes = random.sample(questoes_tema5, len(questoes_tema5))
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
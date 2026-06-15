#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULADOR DE PREPARAÇÃO PARA PROVA - TEMA 3
Curso Técnico em Agronegócio (SENAR)
Módulo: Assessoria, Consultoria e Inovação no Agronegócio
Baseado fielmente no PDF (páginas 64 a 82)
"""

import random
import os

# Banco de questões do TEMA 3
questoes_tema3 = [
    # ===================== TÓPICO 1.1 - LEGISLAÇÃO (p.67) =====================
    {
        "topico": "1.1 Legislação para criação de empresa de consultoria",
        "subt": "Enquadramento jurídico",
        "pergunta": "De acordo com o Sebrae, para abrir um escritório de consultoria, o empreendedor pode ter seu registro de forma individual ou em sociedade. Qual profissional é o mais habilitado para auxiliar na decisão sobre o enquadramento do negócio?",
        "tipo": "mc",
        "opcoes": {
            "a": "Advogado especializado em direito tributário.",
            "b": "Contador.",
            "c": "Engenheiro de produção.",
            "d": "Técnico em agronegócio.",
            "e": "Administrador de empresas."
        },
        "correta": "b",
        "pagina": "67",
        "explicacao": "Página 67: 'O profissional mais habilitado para auxiliar no processo de tomada de decisão sobre o enquadramento do negócio é o contador. Ele poderá ajudar nos atos constitutivos da empresa.'"
    },
    {
        "topico": "1.1 Legislação",
        "subt": "Registro em conselho de classe",
        "pergunta": "Atualmente, os técnicos em agronegócio podem se registrar junto a qual conselho profissional, que migrou do Crea?",
        "tipo": "mc",
        "opcoes": {
            "a": "Conselho Federal de Engenharia e Agronomia (CONFEA).",
            "b": "Conselho Regional de Química (CRQ).",
            "c": "Conselho Federal de Técnicos Agrícolas (CFTA).",
            "d": "Conselho Federal de Administração (CFA).",
            "e": "Ordem dos Advogados do Brasil (OAB)."
        },
        "correta": "c",
        "pagina": "68",
        "explicacao": "Página 68 - Saiba mais: 'Atualmente os técnicos em agronegócio podem se registrar junto ao Conselho Federal de Técnicos Agrícolas (CFTA).'"
    },
    {
        "topico": "1.1 Legislação",
        "subt": "Cooperativa de trabalho",
        "pergunta": "Qual é a maior cooperativa de trabalho no Brasil para o ramo do agronegócio, mencionada no material como oportunidade para prestadores de serviços de consultoria?",
        "tipo": "mc",
        "opcoes": {
            "a": "Coamo.",
            "b": "Sicoob.",
            "c": "Unicampo.",
            "d": "Sicredi.",
            "e": "Embrapa."
        },
        "correta": "c",
        "pagina": "68",
        "explicacao": "Página 68: 'A maior cooperativa de trabalho no Brasil, para o ramo do agronegócio, é a Unicampo.'"
    },
    {
        "topico": "1.1 Legislação",
        "subt": "Documentos necessários",
        "pergunta": "Antes de iniciar as atividades, o consultor deve verificar a necessidade de obtenção de alguns documentos. Assinale a alternativa que NÃO é citada no material como necessária:",
        "tipo": "mc",
        "opcoes": {
            "a": "Alvará de funcionamento.",
            "b": "Licença sanitária.",
            "c": "Registro no conselho de classe.",
            "d": "Certificado de produto orgânico.",
            "e": "Registro na prefeitura."
        },
        "correta": "d",
        "pagina": "67",
        "explicacao": "Página 67: 'Dica: Antes de iniciar suas atividades, o consultor ou time de consultores deverá verificar a necessidade de obtenção de alvará de funcionamento, de licença sanitária e de registro no conselho de classe.' Não há menção a certificado de produto orgânico."
    },

    # ===================== TÓPICO 1.2 - PORTFÓLIO DE SERVIÇOS (p.68-70) =====================
    {
        "topico": "1.2 Portfólio de Serviços",
        "subt": "Equipe multidisciplinar",
        "pergunta": "Para ter um portfólio diversificado de serviços, como o da Unicampo, é preciso contar com profissionais de várias áreas. Qual das seguintes NÃO é citada como área de atuação na cooperativa?",
        "tipo": "mc",
        "opcoes": {
            "a": "Agronomia.",
            "b": "Direito.",
            "c": "Tecnologia da Informação.",
            "d": "Medicina veterinária.",
            "e": "Economia."
        },
        "correta": "d",
        "pagina": "68",
        "explicacao": "Página 68: O portfólio da Unicampo apresenta profissionais de: 'Agronomia, Ecologia, Biologia, Direito, Economia, Engenharias, Tecnologia da Informação, Gestão, entre outras.' Medicina veterinária não consta na lista apresentada."
    },
    {
        "topico": "1.2 Portfólio de Serviços",
        "subt": "Público-alvo e Persona",
        "pergunta": "No material, 'persona' é definida como:",
        "tipo": "mc",
        "opcoes": {
            "a": "O segmento da sociedade com características em comum ao qual se dirige uma estratégia comercial.",
            "b": "Uma representação/descrição de um cliente ideal, baseada em dados e características reais.",
            "c": "O concorrente direto da empresa de consultoria.",
            "d": "O fornecedor de insumos para o agronegócio.",
            "e": "O órgão regulador da atividade de consultoria."
        },
        "correta": "b",
        "pagina": "69",
        "explicacao": "Página 69: 'Persona: É uma representação/descrição de um cliente ideal. Baseia-se em dados e características de clientes reais, como comportamento, dados demográficos, problemas, desafios e objetivos.'"
    },
    {
        "topico": "1.2 Portfólio de Serviços",
        "subt": "Recomendação para iniciantes",
        "pergunta": "Qual a principal recomendação para quem está começando na consultoria, segundo o material, para construir um portfólio?",
        "tipo": "mc",
        "opcoes": {
            "a": "Investir pesado em marketing digital.",
            "b": "Escolher os melhores serviços e projetos já executados em parceria com consultor experiente ou basear-se em casos exitosos anteriores.",
            "c": "Oferecer serviços gratuitos para todos os clientes no primeiro ano.",
            "d": "Focar apenas em um tipo de serviço sem diversificar.",
            "e": "Contratar uma agência de publicidade."
        },
        "correta": "b",
        "pagina": "70",
        "explicacao": "Página 70: 'A principal recomendação dos especialistas nesta área, para quem está começando, é escolher os melhores serviços e projetos de consultoria já executados em parceria com algum consultor que tenha tempo de mercado, ou mesmo basear-se em experiências exitosas de projetos executados anteriormente.'"
    },

    # ===================== TÓPICO 1.3 - PRECIFICAÇÃO (p.70-73) =====================
    {
        "topico": "1.3 Técnicas de precificação",
        "subt": "Benchmarking",
        "pergunta": "A técnica de ter acesso às principais métricas e práticas de negócios da concorrência para compará-las com a realidade da própria empresa é chamada de:",
        "tipo": "mc",
        "opcoes": {
            "a": "Brainstorming.",
            "b": "Benchmarking.",
            "c": "Outbound sales.",
            "d": "Inbound sales.",
            "e": "5W2H."
        },
        "correta": "b",
        "pagina": "71",
        "explicacao": "Página 71: 'Aqui, será possível usar a técnica de benchmarking, que é o processo de ter acesso às principais métricas e práticas de negócios e compará-las com a realidade da sua empresa.'"
    },
    {
        "topico": "1.3 Precificação",
        "subt": "Cobrança por hora vs preço fixo",
        "pergunta": "Verdadeiro ou Falso: O preço fixo reduz as possibilidades de ajustes, pois se o cliente solicitar ações adicionais ao longo do projeto, essas horas não poderão ser cobradas a depender dos termos do contrato.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "71",
        "explicacao": "Página 71: 'O preço fixo, por sua vez, reduz as possibilidades de ajustes. Se, ao longo do caminho, por exemplo, o cliente solicitar mais ações... essas horas não poderão, a depender dos termos do contrato, serem computadas e cobradas ao fim da execução do projeto.'"
    },
    {
        "topico": "1.3 Precificação",
        "subt": "Margem recomendada",
        "pergunta": "Especialistas recomendam que o ideal é sempre trabalhar com margens acima de quanto percentual?",
        "tipo": "mc",
        "opcoes": {
            "a": "50%",
            "b": "100%",
            "c": "150%",
            "d": "200%",
            "e": "300%"
        },
        "correta": "b",
        "pagina": "72",
        "explicacao": "Página 72: 'Especialistas recomendam que o ideal é sempre trabalhar com margens acima de 100%.'"
    },
    {
        "topico": "1.3 Precificação",
        "subt": "Exemplo de cálculo",
        "pergunta": "No exemplo do material, se cada hora de trabalho tem um custo de R$ 25,00, qual deve ser o preço por hora da consultoria seguindo a margem recomendada?",
        "tipo": "mc",
        "opcoes": {
            "a": "R$ 25,00",
            "b": "R$ 37,50",
            "c": "R$ 50,00",
            "d": "R$ 62,50",
            "e": "R$ 75,00"
        },
        "correta": "c",
        "pagina": "72",
        "explicacao": "Página 72 - Caso prático: 'Digamos que, para cada hora de trabalho, você tem um custo de R$ 25,00. Assim, o preço por hora de trabalho da consultoria será de R$ 50,00.' (margem de 100%)."
    },
    {
        "topico": "1.3 Precificação",
        "subt": "Proposta de valor",
        "pergunta": "Verdadeiro ou Falso: O preço é gerado a partir da percepção de valor pelo cliente e sua disponibilidade para pagar. Uma mesma consultoria pode custar valores muito diferentes dependendo de quem oferece e como o cliente percebe o serviço.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "73",
        "explicacao": "Página 73: 'Dica: Venda uma proposta de valor! O preço é gerado a partir da percepção de valor pelo cliente e sua disponibilidade para pagar por um bem ou serviço. Uma mesma consultoria pode custar R$2.000 ou R$60.000 – tudo depende de quem a oferece e como o cliente percebe o serviço.'"
    },

    # ===================== TÓPICO 1.4 - CONTRATOS (p.74-75) =====================
    {
        "topico": "1.4 Orientações para elaboração de contratos",
        "subt": "Vigência do contrato",
        "pergunta": "O material recomenda que, mesmo para projetos complexos, os contratos de consultoria não devem ter vigência muito longa. Qual é o prazo máximo sugerido?",
        "tipo": "mc",
        "opcoes": {
            "a": "3 meses.",
            "b": "6 meses.",
            "c": "12 meses.",
            "d": "18 meses.",
            "e": "24 meses."
        },
        "correta": "b",
        "pagina": "74",
        "explicacao": "Página 74: 'Contratos não devem ter tempos de vigência muito longos, mesmo para projetos complexos e que levarão muitos meses para serem executados. O ideal é que tenham, no máximo, 6 meses.'"
    },
    {
        "topico": "1.4 Contratos",
        "subt": "Relação empregatícia",
        "pergunta": "É importante deixar claro no contrato que a prestação de serviços de consultoria:",
        "tipo": "mc",
        "opcoes": {
            "a": "Estabelece vínculo empregatício entre as partes.",
            "b": "Não estabelece nenhum tipo de relação empregatícia.",
            "c": "Obriga o consultor a cumprir jornada de 8 horas diárias.",
            "d": "Garante férias e 13º salário ao consultor.",
            "e": "Exige carteira de trabalho assinada."
        },
        "correta": "b",
        "pagina": "74",
        "explicacao": "Página 74: 'Também é muito importante deixar claro que esse tipo de contrato não estabelece nenhum tipo de relação empregatícia entre as partes.'"
    },

    # ===================== TÓPICO 2 - PROSPECÇÃO DE CLIENTES (p.76-78) =====================
    {
        "topico": "2. Prospecção de clientes no agronegócio",
        "subt": "Inbound sales",
        "pergunta": "O tipo de vendas pela internet em que a empresa de consultoria cria anúncios em sites de busca e redes sociais para despertar o interesse do potencial cliente é chamado de:",
        "tipo": "mc",
        "opcoes": {
            "a": "Outbound sales.",
            "b": "Inbound sales.",
            "c": "Cold call.",
            "d": "Trade marketing.",
            "e": "Merchandising."
        },
        "correta": "b",
        "pagina": "77",
        "explicacao": "Página 77: 'a) Inbound sales: É um tipo de vendas pela internet. Nela, a empresa de consultoria cria anúncios em sites de busca e em redes sociais a fim de despertar o interesse do potencial cliente em suas soluções.'"
    },
    {
        "topico": "2. Prospecção de clientes",
        "subt": "Outbound sales",
        "pergunta": "Na técnica de outbound sales, quem toma a iniciativa de ir atrás dos potenciais clientes?",
        "tipo": "mc",
        "opcoes": {
            "a": "O cliente procura a consultoria.",
            "b": "Os vendedores do serviço de consultoria.",
            "c): O governo por meio de editais.",
            "d": "As cooperativas indicam os clientes.",
            "e": "Os concorrentes encaminham os clientes."
        },
        "correta": "b",
        "pagina": "78",
        "explicacao": "Página 78: 'b) Outbound sales: Ao contrário da técnica anterior, neste caso são os vendedores do serviço de consultoria quem deverão ir atrás dos potenciais clientes.'"
    },
    {
        "topico": "2. Prospecção de clientes",
        "subt": "Indicação e programas de recomendação",
        "pergunta": "De acordo com Berman (2016), os programas de recomendação podem ser uma forma assertiva e menos custosa que as campanhas tradicionais. O que eles podem oferecer para incentivar as indicações?",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas brindes personalizados.",
            "b": "Descontos, bônus ou qualquer vantagem de negócio.",
            "c": "Participação nos lucros da consultoria.",
            "d": "Cargos de diretoria.",
            "e": "Viagens internacionais."
        },
        "correta": "b",
        "pagina": "78",
        "explicacao": "Página 78: 'As indicações podem ser incentivadas por meio de programas de indicação. O programa pode oferecer descontos, bônus ou qualquer vantagem de negócio.'"
    },
    {
        "topico": "2. Prospecção de clientes",
        "subt": "Uso de celular por produtores",
        "pergunta": "Um estudo da Embrapa em parceria com a ABMR (2020) identificou que percentual de produtores rurais possui celular?",
        "tipo": "mc",
        "opcoes": {
            "a": "68%",
            "b": "79%",
            "c": "85%",
            "d": "94%",
            "e": "99%"
        },
        "correta": "d",
        "pagina": "77",
        "explicacao": "Página 77: 'Um estudo conduzido em 2020 pela Embrapa... identificou que 94% dos produtores rurais têm celulares e, desses, 68% têm smartphones.'"
    },

    # ===================== TÓPICO 3 - TÉCNICAS DE NEGOCIAÇÃO (p.78-82) =====================
    {
        "topico": "3. Técnicas estratégicas de negociação",
        "subt": "Estilos de negociador",
        "pergunta": "Segundo Martin (1982), qual estilo de negociador dá ênfase à inovação, criatividade, exclusividade, grandes projetos e ideias?",
        "tipo": "mc",
        "opcoes": {
            "a": "Apoiador.",
            "b": "Controlador.",
            "c": "Analítico.",
            "d": "Catalisador.",
            "e": "Empreendedor."
        },
        "correta": "d",
        "pagina": "80",
        "explicacao": "Página 80, quadro: 'Catalisador: Ênfase em inovação, criatividade, exclusividade, grandes projetos e ideias.'"
    },
    {
        "topico": "3. Técnicas de negociação",
        "subt": "Estilo Apoiador",
        "pergunta": "O estilo de negociador que tem ênfase em trabalho em equipe, preocupação com pessoas, bem-estar geral e eliminação de conflitos é chamado de:",
        "tipo": "mc",
        "opcoes": {
            "a": "Catalisador.",
            "b": "Controlador.",
            "c": "Apoiador.",
            "d": "Analítico.",
            "e": "Diretivo."
        },
        "correta": "c",
        "pagina": "80",
        "explicacao": "Página 80: 'Apoiador: Ênfase em trabalho em equipe, preocupação com pessoas, no bem-estar geral e na eliminação de conflitos e problemas.'"
    },
    {
        "topico": "3. Técnicas de negociação",
        "subt": "Estilo Controlador",
        "pergunta": "O negociador com ênfase em redução de custos, tempo, prazos, resultados, metas e independência em relação aos outros é classificado como:",
        "tipo": "mc",
        "opcoes": {
            "a": "Catalisador.",
            "b": "Apoiador.",
            "c": "Analítico.",
            "d": "Controlador.",
            "e": "Social."
        },
        "correta": "d",
        "pagina": "80",
        "explicacao": "Página 80: 'Controlador: Ênfase em redução de custos, tempo, prazos, resultados, metas e independência em relação aos outros.'"
    },
    {
        "topico": "3. Técnicas de negociação",
        "subt": "Estilo Analítico",
        "pergunta": "Qual estilo de negociador dá ênfase em informações, dados, detalhes, perfeição e preocupação com o micro?",
        "tipo": "mc",
        "opcoes": {
            "a": "Catalisador.",
            "b": "Apoiador.",
            "c": "Controlador.",
            "d": "Analítico.",
            "e": "Visionário."
        },
        "correta": "d",
        "pagina": "80",
        "explicacao": "Página 80: 'Analítico: Ênfase em informações, dados, detalhes, perfeição, preocupação com o micro.'"
    },
    {
        "topico": "3. Técnicas de negociação",
        "subt": "Fatores estratégicos para negociação",
        "pergunta": "Dentre os fatores estratégicos fundamentais para o sucesso das negociações (Santos, 2009), NÃO é citado:",
        "tipo": "mc",
        "opcoes": {
            "a": "Habilidades pessoais.",
            "b": "Planejamento e organização.",
            "c": "Dominação do cliente.",
            "d": "Flexibilidade e adaptabilidade.",
            "e": "Visão e determinação."
        },
        "correta": "c",
        "pagina": "79",
        "explicacao": "Página 79 lista: habilidades pessoais, planejamento e organização, treinamento e disciplina, autodesenvolvimento, visão, determinação, inovação, alianças, flexibilidade e adaptabilidade. Não consta 'dominação do cliente'."
    },
    {
        "topico": "3. Técnicas de negociação",
        "subt": "Características do cliente do agronegócio",
        "pergunta": "Segundo o Instituto Agro (2019), o cliente do agronegócio, por desembolsar grandes quantidades de dinheiro, tem qual comportamento típico?",
        "tipo": "mc",
        "opcoes": {
            "a": "Decide rapidamente sem muitas informações.",
            "b": "Busca o máximo de informações para ter certeza da melhor compra ou contratação.",
            "c": "Prefere contratar apenas consultorias estrangeiras.",
            "d": "Não se importa com o retorno financeiro.",
            "e": "Sempre negocia apenas por telefone."
        },
        "correta": "b",
        "pagina": "81",
        "explicacao": "Página 81: 'Para o Instituto Agro (2019), o cliente do agronegócio, por desembolsar, com frequência, grandes quantidades de dinheiro para adquirir produtos e serviços, quer sempre ter a certeza de que está fazendo a melhor compra ou contratação. Para ter certeza disso, ele vai sempre buscar o máximo de informações.'"
    }
]

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_resultado(acertos, total):
    print("\n" + "="*70)
    print("   RESULTADO FINAL DO SIMULADOR (TEMA 3)")
    print("="*70)
    print(f"Total de questões: {total}")
    print(f"Acertos: {acertos}")
    print(f"Percentual: {acertos/total*100:.1f}%")
    if acertos/total >= 0.7:
        print("\n🎉 PARABÉNS! Você está preparado para a prova do TEMA 3.")
    elif acertos/total >= 0.5:
        print("\n📚 Bom desempenho! Revise os tópicos onde errou e tente novamente.")
    else:
        print("\n⚠️ Sugerimos revisar o material didático (páginas 64 a 82) antes da prova.")
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
    print("   TEMA 3: MODELO DE NEGÓCIOS PARA PRESTADORES")
    print("          DE SERVIÇOS DE ASSESSORIA E CONSULTORIA")
    print("="*70)
    print(f"\nEste simulador contém {len(questoes_tema3)} questões")
    print("cobrindo todos os tópicos do Tema 3 (páginas 64 a 82).")
    print("\nAs questões podem ser de múltipla escolha (A,B,C,D,E) ou Verdadeiro/Falso (V/F).")
    print("Ao final, você receberá seu percentual de acertos.\n")
    input("Pressione Enter para iniciar...")
    
    # Embaralhar questões
    questoes = random.sample(questoes_tema3, len(questoes_tema3))
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
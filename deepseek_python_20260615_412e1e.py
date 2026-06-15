#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULADOR DE PREPARAÇÃO PARA PROVA - TEMA 6
Curso Técnico em Agronegócio (SENAR)
Módulo: Assessoria, Consultoria e Inovação no Agronegócio
Baseado fielmente no PDF (páginas 115 a 138)
"""

import random
import os

# Banco de questões do TEMA 6
questoes_tema6 = [
    # ===================== INTRODUÇÃO E CONCEITOS GERAIS DE INOVAÇÃO (p.116-118) =====================
    {
        "topico": "Conceitos gerais de inovação",
        "subt": "Definição de Drucker",
        "pergunta": "De acordo com Drucker (1987), a inovação deve ser:",
        "tipo": "mc",
        "opcoes": {
            "a": "Complexa, ampla e orientada para múltiplos objetivos simultâneos.",
            "b": "Simples, focada e orientada para uma aplicação específica, clara e deliberada.",
            "c": "Radical e disruptiva, mudando completamente o mercado.",
            "d": "Exclusivamente tecnológica, envolvendo apenas máquinas e equipamentos.",
            "e": "Baseada apenas em redução de custos."
        },
        "correta": "b",
        "pagina": "116",
        "explicacao": "Página 116: 'Drucker (1987) salienta que a inovação deve ser simples, focada e orientada para uma aplicação específica, clara e deliberada, de modo a satisfazer necessidades pontuais e oferecer um resultado final alinhado ao que foi planejado e executado.'"
    },
    {
        "topico": "Conceitos gerais de inovação",
        "subt": "Inovação incremental vs radical",
        "pergunta": "A inovação incremental é aquela em que:",
        "tipo": "mc",
        "opcoes": {
            "a": "O novo produto ou serviço incorpora novos elementos em relação ao anterior, sem alterar funções básicas.",
            "b": "Algo totalmente novo no mercado traz grande mudança tecnológica, estrutural ou operacional.",
            "c": "Ocorre apenas em grandes empresas multinacionais.",
            "d": "Depende exclusivamente de investimentos governamentais.",
            "e": "Elimina completamente a concorrência."
        },
        "correta": "a",
        "pagina": "117",
        "explicacao": "Página 117: 'Inovação Incremental: Aquela em que o novo produto ou serviço incorpora novos elementos em relação ao anterior, sem que, no entanto, sejam alteradas funções básicas. Inovação Radical: Algo que é novo no mercado e traz uma grande mudança tecnológica, estrutural ou operacional.'"
    },
    {
        "topico": "Conceitos gerais de inovação",
        "subt": "Manual de Oslo",
        "pergunta": "O Manual de Oslo (2005) conceitua inovação como:",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas a invenção de novos produtos tecnológicos.",
            "b": "A implementação de um produto novo ou significativamente melhorado, ou um processo, ou um novo método de marketing, ou um novo método organizacional.",
            "c": "Exclusivamente a melhoria de processos produtivos.",
            "d": "A redução de custos operacionais.",
            "e": "A aquisição de máquinas importadas."
        },
        "correta": "b",
        "pagina": "117",
        "explicacao": "Página 117: 'O Manual de Oslo (2005) conceitua inovação como a implementação de um produto (bem ou serviço), novo ou significativamente melhorado ou um processo ou um novo método de marketing ou, ainda, um novo método organizacional nas práticas de negócios.'"
    },

    # ===================== TÓPICO 1.1 - INOVAÇÃO DE PRODUTO (p.119-122) =====================
    {
        "topico": "1.1 Inovação de produto",
        "subt": "Conceito de inovação de produto",
        "pergunta": "De acordo com o Manual de Oslo (2015), o que pode ser considerada uma inovação de produto?",
        "tipo": "mc",
        "opcoes": {
            "a": "É a implantação e a comercialização de um produto com características aprimoradas, que favorecem os consumidores por meio de novas facilidades e possibilidade de uso.",
            "b": "É a adoção de métodos de produção novos ou significativamente melhorados.",
            "c": "É a transformação nos métodos de negócio da empresa.",
            "d": "É a mudança na organização do local do trabalho.",
            "e": "É a criação de uma nova campanha publicitária."
        },
        "correta": "a",
        "pagina": "119",
        "explicacao": "Página 119: 'Uma inovação tecnológica de produto consiste na implantação e comercialização de um bem com características aprimoradas, que favorecem de forma significativa os consumidores por meio de novas facilidades ou possibilidades de uso.'"
    },
    {
        "topico": "1.1 Inovação de produto",
        "subt": "Produto tecnologicamente novo vs aprimorado",
        "pergunta": "Verdadeiro ou Falso: Um produto tecnologicamente novo é aquele cujas características tecnológicas ou usos pretendidos diferem dos produzidos anteriormente, podendo envolver tecnologias radicalmente novas.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "120",
        "explicacao": "Página 120: 'Produto tecnologicamente novo: É um produto cujas características tecnológicas ou usos pretendidos diferem dos produzidos anteriormente. Tais inovações podem envolver tecnologias radicalmente novas.'"
    },
    {
        "topico": "1.1 Inovação de produto",
        "subt": "Exemplo do escorredor de arroz",
        "pergunta": "O exemplo do escorredor de arroz, inventado por Therezinha Beatriz Zorowich em 1959, serve para demonstrar que:",
        "tipo": "mc",
        "opcoes": {
            "a": "Inovação de produto só ocorre com alto nível de tecnologia embarcada.",
            "b": "Inovação de produto não está somente em bens com alta tecnologia; pequenas mudanças também podem ser inovações aceitas pelo mercado.",
            "c": "Apenas grandes corporações conseguem inovar.",
            "d": "Inovação requer investimentos milionários.",
            "e": "O Brasil não produz inovações relevantes."
        },
        "correta": "b",
        "pagina": "122",
        "explicacao": "Página 122: 'O exemplo do escorredor de arroz serve para demonstrar que inovação de produto não está somente nos casos de bens com alto nível de tecnologia embarcada e transformações que envolvem elevados custos. É preciso pensar em pequenas mudanças.'"
    },

    # ===================== TÓPICO 1.2 - INOVAÇÃO DE PROCESSO (p.123-124) =====================
    {
        "topico": "1.2 Inovação de processo",
        "subt": "Conceito de inovação de processo",
        "pergunta": "A inovação tecnológica de processo consiste na adoção de métodos de produção novos ou significativamente melhorados. Qual é um dos principais objetivos desse tipo de inovação?",
        "tipo": "mc",
        "opcoes": {
            "a": "Aumentar o preço dos produtos.",
            "b": "Reduzir custos, tempo e a complexidade de processos internos.",
            "c": "Eliminar a necessidade de mão de obra.",
            "d": "Criar novos mercados exclusivamente.",
            "e": "Substituir todos os equipamentos por outros mais caros."
        },
        "correta": "b",
        "pagina": "123",
        "explicacao": "Página 123: 'Considera-se a necessidade desse tipo de inovação para reduzir custos, tempo e a complexidade de processos internos, sempre com o objetivo de melhorar os resultados.'"
    },
    {
        "topico": "1.2 Inovação de processo",
        "subt": "Exemplo morango semi-hidropônico",
        "pergunta": "No exemplo do cultivo de morango, a mudança do sistema convencional (canteiros no solo) para o sistema semi-hidropônico (estufa com bancadas elevadas) é considerada uma inovação de:",
        "tipo": "mc",
        "opcoes": {
            "a": "Produto.",
            "b": "Processo.",
            "c": "Marketing.",
            "d": "Organizacional.",
            "e": "Financeira."
        },
        "correta": "b",
        "pagina": "124",
        "explicacao": "Página 124: 'Mudar de um modelo de produção convencional para um sistema semi-hidropônico é uma inovação de processos.'"
    },

    # ===================== TÓPICO 1.3 - INOVAÇÃO DE MARKETING (p.124-126) =====================
    {
        "topico": "1.3 Inovação de marketing",
        "subt": "Conceito e objetivo",
        "pergunta": "A inovação de marketing tem como grande objetivo:",
        "tipo": "mc",
        "opcoes": {
            "a": "Reduzir o preço dos produtos a qualquer custo.",
            "b": "A captura de mercados para produtos e processos tecnologicamente novos ou aprimorados.",
            "c": "Substituir o produto existente por outro completamente diferente.",
            "d": "Eliminar a concorrência por meio de ações agressivas.",
            "e": "Focar apenas em promoções sazonais."
        },
        "correta": "b",
        "pagina": "126",
        "explicacao": "Página 126: 'A captura de mercados para produtos e processos tecnologicamente novos ou aprimorados é classificada como o grande objetivo do marketing e quando isso acontece considera-se que ocorreu uma inovação de marketing.'"
    },
    {
        "topico": "1.3 Inovação de marketing",
        "subt": "O que NÃO é inovação de marketing",
        "pergunta": "Segundo o Manual de Oslo (2015), não é considerada inovação de marketing quando:",
        "tipo": "mc",
        "opcoes": {
            "a": "Uma ação de marketing é executada para promover um novo produto tecnológico.",
            "b": "Uma ação de marketing é executada puramente para promover mudanças organizacionais de rotina (ex: campanha para promover nova estrutura da empresa).",
            "c": "Uma ação de marketing divulga um novo processo produtivo.",
            "d": "Uma pesquisa de comportamento do consumidor é realizada antes do lançamento.",
            "e": "Uma nova embalagem é criada para um produto melhorado."
        },
        "correta": "b",
        "pagina": "126",
        "explicacao": "Página 126: 'Não consideramos uma inovação de marketing quando uma ação nessa área é executada puramente para promover mudanças organizacionais de rotina. Por exemplo, uma campanha para promover novas estruturas e a imagem corporativa de uma empresa.'"
    },

    # ===================== TÓPICO 1.4 - INOVAÇÕES ORGANIZACIONAIS (p.126-128) =====================
    {
        "topico": "1.4 Inovações organizacionais",
        "subt": "Conceito e condições",
        "pergunta": "De acordo com o Manual de Oslo (2015), a inovação organizacional pode incluir: introdução de estruturas organizacionais significativamente alteradas, implantação de técnicas de gerenciamento avançado e implantação de orientações estratégicas novas. No entanto, a mudança organizacional só é considerada inovação se:",
        "tipo": "mc",
        "opcoes": {
            "a": "For aprovada por todos os funcionários.",
            "b": "Houver mudanças mensuráveis nos resultados, como aumento de produtividade ou de vendas.",
            "c": "Envolver a demissão de funcionários.",
            "d": "For implementada por uma consultoria externa.",
            "e": "Durar mais de um ano."
        },
        "correta": "b",
        "pagina": "127",
        "explicacao": "Página 127: 'A princípio, a mudança organizacional conta como inovação apenas se houver mudanças mensuráveis nos resultados, tais como aumento de produtividade ou de vendas.'"
    },
    {
        "topico": "1.4 Inovações organizacionais",
        "subt": "Treinamento como inovação?",
        "pergunta": "Verdadeiro ou Falso: O treinamento de pessoal, por si só, é considerado uma inovação organizacional segundo o Manual de Oslo (2015).",
        "tipo": "vf",
        "correta": "F",
        "pagina": "127",
        "explicacao": "Página 127: 'É preciso ficar claro para o mercado e para a gestão da inovação nas empresas que, para o entendimento estabelecido no Manual de Oslo (2015), não se pode considerar inovação treinamento de pessoal. Treinamentos de rotina também não são um exemplo de inovação.'"
    },

    # ===================== TÓPICO 2 - FATORES QUE INFLUENCIAM A INOVAÇÃO (p.129-133) =====================
    {
        "topico": "2. Fatores que influenciam a inovação em empresas rurais",
        "subt": "Definição de empresa rural",
        "pergunta": "De acordo com Marion (2017), empresa rural é aquela que:",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas cultiva a terra, sem criação de animais.",
            "b": "Explora a capacidade produtiva do solo por meio do cultivo da terra, da criação de animais e da transformação de determinados produtos agrícolas.",
            "c": "Somente processa produtos agropecuários.",
            "d": "Apenas comercializa insumos agrícolas.",
            "e": "Exclusivamente presta serviços de consultoria."
        },
        "correta": "b",
        "pagina": "129",
        "explicacao": "Página 129: 'empresa rural: são aquelas que exploram a capacidade produtiva do solo por meio do cultivo da terra, da criação de animais e da transformação de determinados produtos agrícolas (MARION, 2017).'"
    },
    {
        "topico": "2. Fatores que influenciam a inovação",
        "subt": "Motivação principal para inovar",
        "pergunta": "Qual é a principal motivação para que as empresas rurais inovem, segundo o material?",
        "tipo": "mc",
        "opcoes": {
            "a": "Aumentar o número de funcionários.",
            "b": "Reduzir seus custos de produção, aumentar a produtividade e a lucratividade.",
            "c": "Atender exigências exclusivas do mercado externo.",
            "d": "Substituir toda a mão de obra por robôs.",
            "e": "Tornar-se uma organização sem fins lucrativos."
        },
        "correta": "b",
        "pagina": "130-131",
        "explicacao": "Página 130-131: 'Você já parou para pensar em por que as empresas rurais inovam? Porque querem reduzir seus custos de produção, aumentar a produtividade e, por consequência, obter o aumento de sua lucratividade. Inevitavelmente, a principal motivação para que as empresas rurais inovem é a superação de problemas estruturais.'"
    },
    {
        "topico": "2. Fatores que influenciam a inovação",
        "subt": "Tipos de crédito rural",
        "pergunta": "De acordo com o Banco Central (2021), o crédito de custeio destina-se a:",
        "tipo": "mc",
        "opcoes": {
            "a": "Aplicações em bens ou serviços cujo benefício se estenda por vários períodos de produção (ex: compra de trator).",
            "b": "Cobrir despesas normais dos ciclos produtivos, da compra de insumos à fase de colheita.",
            "c": "Viabilizar a comercialização de produtos no mercado.",
            "d": "Industrialização de produtos agropecuários.",
            "e": "Exportação de commodities."
        },
        "correta": "b",
        "pagina": "132",
        "explicacao": "Página 132: 'Crédito de custeio: Destina-se a cobrir despesas normais dos ciclos produtivos, da compra de insumos à fase de colheita.'"
    },
    {
        "topico": "2. Fatores que influenciam a inovação",
        "subt": "Seguro rural",
        "pergunta": "O objetivo maior do Seguro Rural, de acordo com a SUSEP (2021), é:",
        "tipo": "mc",
        "opcoes": {
            "a": "Garantir lucro mínimo ao produtor.",
            "b": "Oferecer coberturas que atendam ao produtor, à produção, à família e à geração de garantias a financiadores, diluindo riscos.",
            "c": "Substituir o crédito rural.",
            "d": "Financiar a compra de máquinas.",
            "e": "Garantir a exportação de toda a produção."
        },
        "correta": "b",
        "pagina": "133",
        "explicacao": "Página 133: 'O objetivo maior do Seguro Rural é oferecer coberturas que, simultaneamente, atendam ao produtor à sua produção, à sua família, à geração de garantias a seus financiadores, investidores, parceiros de negócios, todos interessados na maior diluição possível dos riscos.'"
    },

    # ===================== TÓPICO 3 - AMBIÊNCIA INOVADORA (p.133-138) =====================
    {
        "topico": "3. Benefícios da ambiência inovadora",
        "subt": "Diferença entre ambiente inovador e ambiência inovadora",
        "pergunta": "No material, define-se que 'ambiente inovador' se refere ao contexto interno de uma empresa, enquanto 'ambiência inovadora' se refere:",
        "tipo": "mc",
        "opcoes": {
            "a": "Exclusivamente ao governo federal.",
            "b": "À combinação de ações e fatores mobilizados por diferentes instituições com o objetivo de criar um ambiente inovador em várias empresas de uma cadeia produtiva.",
            "c": "Apenas às condições climáticas favoráveis.",
            "d": "Ao espaço físico do escritório de consultoria.",
            "e": "Às máquinas e equipamentos de última geração."
        },
        "correta": "b",
        "pagina": "134",
        "explicacao": "Página 134: 'Definimos que ambiente inovador se refere ao contexto interno de uma determinada empresa. Já a ambiência inovadora se refere à combinação de ações e fatores mobilizados por diferentes instituições com o objetivo de criar um ambiente inovador em várias empresas de uma cadeia produtiva.'"
    },
    {
        "topico": "3. Ambiência inovadora",
        "subt": "Identificação de problemas",
        "pergunta": "Segundo o material, qual é o primeiro passo para uma possível solução inovadora?",
        "tipo": "mc",
        "opcoes": {
            "a": "Contratar uma consultoria cara.",
            "b": "Identificar os problemas de forma clara.",
            "c": "Comprar novas máquinas.",
            "d": "Demitir funcionários.",
            "e": "Aumentar a produção."
        },
        "correta": "b",
        "pagina": "135",
        "explicacao": "Página 135: 'Identificar os problemas de forma clara é o primeiro passo para uma possível solução. Ou seja, numa ambiência inovadora, os agentes... podem se organizar para propor um rol de possíveis soluções.'"
    },
    {
        "topico": "3. Ambiência inovadora",
        "subt": "Como as empresas se aproveitam da ambiência inovadora",
        "pergunta": "De acordo com Oliveira e Silva (2016), as empresas podem se aproveitar da ambiência inovadora por meio de:",
        "tipo": "mc",
        "opcoes": {
            "a": "Isolamento do mercado.",
            "b": "Participação em palestras e cursos, absorção de tecnologia, busca por informações em seminários, obtenção de programas de apoio do governo e informações dos colaboradores.",
            "c": "Apenas comprando tecnologias prontas.",
            "d": "Esperando incentivos governamentais exclusivamente.",
            "e": "Reduzindo o quadro de funcionários."
        },
        "correta": "b",
        "pagina": "135",
        "explicacao": "Página 135: 'As empresas conseguem se aproveitar dessa ambiência inovadora, por exemplo, por meio de participação em palestras e cursos, absorção de algum tipo de tecnologia, busca por informações em seminários e congressos, aquisição de informações técnicas, como patentes, obtenção de programas de apoio do governo e por informações colhidas dos colaboradores (Oliveira & Silva, 2016).'"
    },
    {
        "topico": "3. Ambiência inovadora",
        "subt": "Programa Agro 4.0",
        "pergunta": "Em 2021, o Mapa lançou o Programa Agro 4.0 com um montante de recursos financeiros destinados ao financiamento do uso de tecnologias 4.0 por produtores rurais. Qual foi o valor mencionado no material?",
        "tipo": "mc",
        "opcoes": {
            "a": "R$ 1,2 milhão.",
            "b": "R$ 2,5 milhões.",
            "c": "R$ 4,8 milhões.",
            "d": "R$ 10 milhões.",
            "e": "R$ 50 milhões."
        },
        "correta": "c",
        "pagina": "137",
        "explicacao": "Página 137: 'em 2021, o Mapa lançou o Programa Agro 4.0, com um montante de R$ 4,8 milhões destinados ao financiamento do uso de tecnologias 4.0 por produtores rurais.'"
    },
    {
        "topico": "3. Ambiência inovadora",
        "subt": "Sistema CNA",
        "pergunta": "De acordo com a CNA (2020), quantos sindicatos rurais compõem a base do Sistema CNA?",
        "tipo": "mc",
        "opcoes": {
            "a": "957 sindicatos.",
            "b": "1.500 sindicatos.",
            "c": "1.957 sindicatos rurais e 1.130 extensões de base.",
            "d": "2.500 sindicatos.",
            "e": "3.000 sindicatos."
        },
        "correta": "c",
        "pagina": "136",
        "explicacao": "Página 136: 'A entidade tem, em sua base, 1.957 sindicatos rurais e 1.130 extensões de base, segundo dados do Departamento Sindical – Desin, em 30/11/2019.'"
    }
]

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_resultado(acertos, total):
    print("\n" + "="*70)
    print("   RESULTADO FINAL DO SIMULADOR (TEMA 6)")
    print("="*70)
    print(f"Total de questões: {total}")
    print(f"Acertos: {acertos}")
    print(f"Percentual: {acertos/total*100:.1f}%")
    if acertos/total >= 0.7:
        print("\n🎉 PARABÉNS! Você está preparado para a prova do TEMA 6.")
    elif acertos/total >= 0.5:
        print("\n📚 Bom desempenho! Revise os tópicos onde errou e tente novamente.")
    else:
        print("\n⚠️ Sugerimos revisar o material didático (páginas 115 a 138) antes da prova.")
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
    print("   TEMA 6: O PAPEL DOS SERVIÇOS DE CONSULTORIA")
    print("          PARA A INOVAÇÃO NO AGRONEGÓCIO")
    print("="*70)
    print(f"\nEste simulador contém {len(questoes_tema6)} questões")
    print("cobrindo todos os tópicos do Tema 6 (páginas 115 a 138).")
    print("\nAs questões podem ser de múltipla escolha (A,B,C,D,E) ou Verdadeiro/Falso (V/F).")
    print("Ao final, você receberá seu percentual de acertos.\n")
    input("Pressione Enter para iniciar...")
    
    # Embaralhar questões
    questoes = random.sample(questoes_tema6, len(questoes_tema6))
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
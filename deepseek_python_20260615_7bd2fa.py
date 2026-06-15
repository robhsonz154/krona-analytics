#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz: Atividades de Aprendizagem - Curso Técnico em Agronegócio (SENAR)
Módulo: Assessoria, Consultoria e Inovação no Agronegócio
Baseado fielmente no material didático (páginas 19 a 128)
"""

import sys

# Estrutura das questões
# tipo: 'mc' = múltipla escolha, 'open' = aberta (dissertativa)
questoes = [
    # TEMA 1 - Conceitos básicos de assessoria e consultoria no agronegócio
    {
        "tema": 1,
        "pagina": 19,
        "texto": "Conforme estudamos, os serviços de assessoria estão cada vez mais amplos e completos. Englobam processos de produção, serviços gerenciais e organizacionais para empresas e instituições que se encontram antes, dentro e depois da porteira. Com base nisso, assinale a alternativa que indica corretamente o papel do assessor na prestação de serviços técnicos gerenciais para empresas do agronegócio.",
        "tipo": "mc",
        "opcoes": {
            "a": "O assessor deve agir como um colaborador interno, que responde às demandas de seus superiores sempre que demandado.",
            "b": "O papel do assessor é elaborar estratégias com base em estudos sobre o mercado de atuação de cada empresa para implementá-las de forma eficaz e, depois, informar os donos da empresa sobre os resultados.",
            "c": "O papel do assessor é fazer um levantamento de estratégias diferentes de preparação e planejamento dos negócios, sempre com foco na melhoria de produtividade e desempenho estratégico das empresas em que atua.",
            "d": "O assessor técnico precisa combinar conhecimentos, habilidades e atitudes que só um profissional de nível sênior consegue ter.",
            "e": "O papel do assessor é fazer com que a empresa esteja sempre atualizada sobre políticas públicas, mudanças nos cenários político e institucional no país e no mundo."
        },
        "correta": "c",
        "explicacao": "Conforme Cruz (2008), o papel do assessor é fazer um levantamento de estratégias diferentes de preparação e planejamento dos negócios, sempre com foco na melhoria de produtividade e desempenho estratégico."
    },
    {
        "tema": 1,
        "pagina": 19,
        "texto": "Os serviços de assessoria e consultoria têm papéis integrados e complementares. Entretanto, vale ressaltar algumas diferenças entre essas duas formas de prestação de serviços. Qual é a principal diferença entre assessoria e consultoria, que podemos considerar, a partir do conteúdo estudado?",
        "tipo": "mc",
        "opcoes": {
            "a": "A consultoria tem como base propósito bem definido e as datas para o seu início e fim são mais claras para os contratantes. Já a assessoria pode ser mais duradoura e contar com uma relação mais próxima e contínua com as empresas.",
            "b": "A consultoria tem caráter complexo e permanente, pois muitos negócios adotam esse modelo de contratação para seus colaboradores, pois a assessoria é sempre terceirizada.",
            "c": "A assessoria empresarial tem mais mercado e oportunidades, e a consultoria é restrita às grandes empresas multinacionais.",
            "d": "A assessoria e consultoria empresarial não apresentam diferenças, somente complementaridades entre si.",
            "e": "Os serviços de consultoria só podem ser prestados por empresas especializadas e registradas em conselhos de classe profissional. Já a assessoria é livre e independe de tais registros."
        },
        "correta": "a",
        "explicacao": "A consultoria tem caráter transitório (começo, meio e fim bem definidos), enquanto a assessoria é mais complexa, de longo prazo e com maior envolvimento no contexto interno da organização."
    },
    {
        "tema": 1,
        "pagina": 29,
        "texto": "Por que a busca por responsabilidade social e ambiental será uma das principais causas de buscas por serviços de consultoria nas próximas décadas?",
        "tipo": "open",
        "resposta_esperada": "Está surgindo o conceito ESG (environmental, social and governance), que representa questões relativas à sustentabilidade ambiental, social e de governança corporativa. O objetivo das organizações deve ir além de evitar a deterioração dos recursos naturais; é preciso combater a ausência de práticas organizacionais voltadas às políticas sociais. O mercado consumidor requer modelos de gestão transparentes, íntegros e comprometidos com o bem-estar social."
    },
    {
        "tema": 1,
        "pagina": 31,
        "texto": "Qual é o nível de consultoria que atua em um ou poucos assuntos dentro de uma área de conhecimento?",
        "tipo": "mc",
        "opcoes": {
            "a": "Consultoria de pacote.",
            "b": "Consultoria artesanal.",
            "c": "Consultoria global.",
            "d": "Consultoria especializada.",
            "e": "Consultoria total."
        },
        "correta": "d",
        "explicacao": "A consultoria especializada atua em um ou poucos assuntos dentro de uma área de conhecimento, como a aplicação da NR 31 na empresa rural."
    },
    {
        "tema": 1,
        "pagina": 31,
        "texto": "Com base nos seus estudos até aqui, defina o que é consultoria de pacote e cite um exemplo.",
        "tipo": "open",
        "resposta_esperada": "Consultoria de pacote é aquela prestada de forma padrão e previamente constituída, sem profundo conhecimento da realidade da empresa. Exemplo: o cliente liga para a empresa de consultoria solicitando uma ferramenta de gestão de estoque; a consultoria implementa a ferramenta sem fazer um diagnóstico completo do cliente."
    },
    {
        "tema": 1,
        "pagina": 31,
        "texto": "Defina o que é consultoria artesanal e cite um exemplo.",
        "tipo": "open",
        "resposta_esperada": "Consultoria artesanal (ou personalizada) preocupa-se em atender às necessidades do cliente por meio de um projeto baseado em metodologias e técnicas especificamente estruturadas para a situação. Exemplo: um projeto customizado de planejamento estratégico para uma empresa rural, considerando suas particularidades organizacionais."
    },
    {
        "tema": 1,
        "pagina": 39,
        "texto": "A prestação de serviços em formato de consultoria é uma boa opção para os técnicos em agronegócio. De acordo com os estudos realizados, qual é o conceito de consultoria?",
        "tipo": "mc",
        "opcoes": {
            "a": "Pode ser definida como ação estruturada para a área de gestão financeira.",
            "b": "É uma prestação de serviços específica para empresas que querem entrar no mercado.",
            "c": "É um acompanhamento constante, onde os profissionais interagem com as melhores empresas de cada setor.",
            "d": "É um processo interativo de um agente de mudanças externo à empresa.",
            "e": "Pode ser entendida como um processo de triangulação de conhecimentos entre empresas, governo e escritórios de consultoria."
        },
        "correta": "d",
        "explicacao": "Consultoria é um processo interativo de um agente de mudanças externo à empresa, que auxilia os executivos nas tomadas de decisão, sem ter controle direto da situação (Oliveira, 2009)."
    },
    {
        "tema": 1,
        "pagina": 39,
        "texto": "Diante do padrão de conceitos e estudos adotados, o que pode ser entendido como ato de inovar?",
        "tipo": "mc",
        "opcoes": {
            "a": "Inovar é essencial para que as empresas se mantenham de forma competitiva e sustentável no mercado.",
            "b": "Inovar ajuda as empresas a manterem seus níveis de custos elevados em prol de retornos no futuro.",
            "c": "Inovar é uma prática muito comum entre as empresas rurais de pequeno e médio porte.",
            "d": "Inovar é obrigatório para que as empresas tenham mais tempo para tomar decisões.",
            "e": "Inovar é essencial para que a sustentabilidade dos negócios rurais seja reduzida."
        },
        "correta": "a",
        "explicacao": "Inovar é essencial para manter a competitividade e a sustentabilidade no mercado, conforme abordado no material."
    },
    {
        "tema": 1,
        "pagina": 39,
        "texto": "No Brasil, entende-se por inovação a introdução de novidade ou aperfeiçoamento no ambiente produtivo ou social que resulte em novos produtos, processos ou serviços. Contudo, há outras definições de inovação. Cite um outro conceito aceito que defina o que é inovação.",
        "tipo": "open",
        "resposta_esperada": "Uma nova ideia implementada com sucesso, que produz resultados econômicos; ou ter ideias que seus concorrentes ainda não tiveram e implantá-las com sucesso; ou inovação em produtos, serviços, processos, negócios ou na gestão."
    },
    {
        "tema": 1,
        "pagina": 40,
        "texto": "Qual das opções elencadas a seguir não pode ser diretamente definida como uma das vantagens para organizações que contratam serviços de consultoria?",
        "tipo": "mc",
        "opcoes": {
            "a": "Crescimento do negócio.",
            "b": "Conhecimento sustentado.",
            "c": "Criatividade.",
            "d": "Agilidade na aprendizagem.",
            "e": "Eliminar concorrentes."
        },
        "correta": "e",
        "explicacao": "A consultoria não elimina concorrentes, mas ajuda a entendê-los e agir estrategicamente diante deles."
    },
    # TEMA 2 - Tendências e perspectivas
    {
        "tema": 2,
        "pagina": 50,
        "texto": "Qual é o tipo de estratégia que uma empresa deve adotar quando não tem mais alternativas e se encontra em uma situação caótica?",
        "tipo": "mc",
        "opcoes": {
            "a": "Estratégia de sobrevivência.",
            "b": "Estratégia de manutenção.",
            "c": "Estratégia de desenvolvimento.",
            "d": "Estratégia de marketing.",
            "e": "Estratégia de venda."
        },
        "correta": "a",
        "explicacao": "Estratégia de sobrevivência: adotada quando a empresa não tem mais alternativas e se encontra em situação caótica, focando em parar investimentos, reduzir despesas e solucionar problemas graves."
    },
    {
        "tema": 2,
        "pagina": 63,
        "texto": "Um profissional, para atuar na gestão do agronegócio, deve unir conhecimentos técnicos, próprios da atividade da produção agropecuária e do processamento de seus produtos, a uma sólida formação em gestão. Com base nisso, qual das áreas a seguir não faz parte do rol de setores potencialmente mais adequados para a atuação do técnico em agronegócio?",
        "tipo": "mc",
        "opcoes": {
            "a": "Gestão da produção.",
            "b": "Aplicação de insumos.",
            "c": "Organização financeira e de custos.",
            "d": "Mapeamento logística e da cadeia de suprimentos.",
            "e": "Gestão de pessoas."
        },
        "correta": "b",
        "explicacao": "A aplicação de insumos é uma atividade característica dos técnicos em agropecuária ou técnicos agrícolas, não sendo o foco principal do técnico em agronegócio, que atua mais na gestão."
    },
    # TEMA 3 - Modelo de negócios
    {
        "tema": 3,
        "pagina": 75,
        "texto": "Qual das possibilidades a seguir pode ser considerada para a constituição e a formalização de uma organização que presta serviços de consultoria?",
        "tipo": "mc",
        "opcoes": {
            "a": "Cooperativa de trabalho.",
            "b": "Associação sem fins lucrativos.",
            "c": "Organização não governamental.",
            "d": "Instituição de ensino.",
            "e": "Parque tecnológico."
        },
        "correta": "a",
        "explicacao": "A cooperativa de trabalho é uma oportunidade pouco explorada mas adequada para quem presta serviços de consultoria, como a Unicampo."
    },
    {
        "tema": 3,
        "pagina": 75,
        "texto": "Quais os principais fatores que devem ser considerados na hora de precificar um serviço de consultoria?",
        "tipo": "open",
        "resposta_esperada": "Devem ser considerados: a experiência do consultor no mercado; a base de preço da hora de consultoria recomendada por conselhos de classe; os custos fixos e variáveis; a margem de retorno financeiro pretendida; o comportamento da concorrência (benchmarking); a escolha entre cobrar por hora ou preço fixo; e os custos com deslocamentos, alimentação, tributos, etc."
    },
    {
        "tema": 3,
        "pagina": 81,
        "texto": "Dentro do processo de negociação verifica-se que existem diversos estilos de negociação. Qual o estilo do negociador que dá 'ênfase em informações, dados, detalhes, perfeição e tem preocupação com o micro'?",
        "tipo": "mc",
        "opcoes": {
            "a": "Catalisador.",
            "b": "Apoiador.",
            "c": "Controlador.",
            "d": "Analítico.",
            "e": "Empreendedor."
        },
        "correta": "d",
        "explicacao": "O estilo analítico é caracterizado pela ênfase em informações, dados, detalhes, perfeição e preocupação com o micro."
    },
    # TEMA 4 - Macro e microambiente
    {
        "tema": 4,
        "pagina": 89,
        "texto": "Veja as descrições a seguir e verifique a quais conceitos se referem: I. É composto por forças que afetam o microambiente e o nível interno das organizações, onde diferentes forças se combinam e atuam diretamente no comportamento delas, que não têm como controlar esse fenômeno. II. É composto por forças mobilizadas por agentes e instituições mais diretamente ligadas à determinada empresa. Na sequência, marque a única alternativa correta:",
        "tipo": "mc",
        "opcoes": {
            "a": "O primeiro item se refere ao conceito de microambiente, e o segundo, ao de macroambiente.",
            "b": "O primeiro item se refere ao conceito de macroambiente, e o segundo, ao de microambiente.",
            "c": "O primeiro item se refere ao conceito de gestão estratégica, e o segundo, ao de gestão de políticas públicas.",
            "d": "O primeiro item se refere ao conceito de microempresa, e o segundo, ao de empresa de grande porte.",
            "e": "O primeiro item se refere ao conceito de ambiente amplo de negócios, e o segundo, ao de ambiente prático de negócios."
        },
        "correta": "b",
        "explicacao": "Macroambiente: forças externas que a empresa não controla. Microambiente: forças mais próximas e com maior controle."
    },
    # TEMA 5 - Diagnóstico socioprodutivo, econômico e ambiental
    {
        "tema": 5,
        "pagina": 102,
        "texto": "Qual dos itens a seguir não é necessário considerar em um plano de ação desenvolvido com base na técnica 5W2H?",
        "tipo": "mc",
        "opcoes": {
            "a": "O que será feito?",
            "b": "Quanto vai custar cada ação?",
            "c": "Onde será aplicada cada ação?",
            "d": "Quando será executada cada ação?",
            "e": "Quantas linhas de crédito existem para cada ação?"
        },
        "correta": "e",
        "explicacao": "A técnica 5W2H envolve: What, Why, Where, When, Who, How, How much. Não envolve o número de linhas de crédito."
    },
    {
        "tema": 5,
        "pagina": 102,
        "texto": "Qual é a técnica de análise do contexto empresarial que contribui para identificar forças, oportunidades, fraquezas e ameaças de um determinado negócio?",
        "tipo": "mc",
        "opcoes": {
            "a": "Método 5W2H",
            "b": "Análise de concorrentes",
            "c": "Análise Swot",
            "d": "Método de análise 'Entra e Sai'",
            "e": "Benchmarking"
        },
        "correta": "c",
        "explicacao": "A análise Swot (ou Fofa) é a técnica que identifica forças, oportunidades, fraquezas e ameaças."
    },
    {
        "tema": 5,
        "pagina": 107,
        "texto": "A partir do conteúdo estudado, marque a única alternativa que apresente corretamente a definição de Diagnóstico Rural Participativo.",
        "tipo": "mc",
        "opcoes": {
            "a": "O Diagnóstico Rural Participativo é um conjunto de técnicas e ferramentas que permite a obtenção direta de informação primária ou de campo, de modo que os atores sociais participam ativamente do processo.",
            "b": "O Diagnóstico Rural Participativo é uma técnica das empresas de assistência e extensão rural públicas, como a Emater.",
            "c": "O Diagnóstico Rural Participativo é um conjunto de técnicas aplicadas em grandes empresas rurais.",
            "d": "O Diagnóstico Rural Participativo é mais indicado para as agroindústrias, pois indica as melhores práticas de produção.",
            "e": "O Diagnóstico Rural Participativo é um conjunto de técnicas e ferramentas para a formulação de ações governamentais."
        },
        "correta": "a",
        "explicacao": "O DRP permite que os atores sociais (agricultores) participem do diagnóstico de seu próprio ambiente, conforme Chambers (1982)."
    },
    {
        "tema": 5,
        "pagina": 113,
        "texto": "Qual é o principal diferencial da metodologia ATeG/SENAR?",
        "tipo": "mc",
        "opcoes": {
            "a": "Nela, os produtores têm acesso a um modelo único de assessoria, pois as dimensões gerenciais e organizacionais das propriedades rurais são devidamente analisadas, e não somente as questões relacionadas aos sistemas produtivos de forma isolada.",
            "b": "O maior diferencial da ATeG/SENAR é o acompanhamento contínuo do negócio rural por mais de 4 anos.",
            "c": "O grande diferencial da ATeG/SENAR é o foco nas questões relacionadas às melhores práticas de produção agropecuária.",
            "d": "O grande diferencial da metodologia ATeG/SENAR é o foco na coordenação e na gestão de pessoas das principais cadeias produtivas do país.",
            "e": "A metodologia tem foco na gestão dos custos totais dos sistemas de produção das empresas rurais da cadeia produtiva da bovinocultura de leite."
        },
        "correta": "a",
        "explicacao": "A ATeG/SENAR analisa as dimensões gerenciais e organizacionais, não apenas os sistemas produtivos isoladamente."
    },
    {
        "tema": 5,
        "pagina": 113,
        "texto": "Qual dos itens a seguir não pode ser apontado como um dos objetivos da ATeG/SENAR?",
        "tipo": "mc",
        "opcoes": {
            "a": "Capacitar o produtor rural para o empreendedorismo e a gestão do negócio.",
            "b": "Elevar a renda e a produtividade da propriedade rural por meio do aumento da eficiência e da eficácia.",
            "c": "Aumentar a rentabilidade dos negócios rurais.",
            "d": "Estabelecer o perfil e o comportamento dos consumidores finais das cadeias produtivas do agronegócio.",
            "e": "Elaborar o planejamento estratégico da propriedade rural."
        },
        "correta": "d",
        "explicacao": "A ATeG/SENAR não tem como objetivo pesquisar o comportamento dos consumidores finais, mas sim melhorar a gestão e produtividade da propriedade."
    },
    {
        "tema": 5,
        "pagina": 113,
        "texto": "De acordo com o que você estudou até o momento, o que uma empresa deve fazer para ser considerada inovadora?",
        "tipo": "mc",
        "opcoes": {
            "a": "Para que uma empresa seja inovadora, deve implementar ações em diferentes direções enquanto existir no mercado, bem como implementar, de alguma forma, novos produtos, processos gerenciais, ou uma combinação de ambos.",
            "b": "Para que uma empresa seja inovadora, deve gerar consideráveis impactos sociais e mercadológicos que mudem as características econômicas do país.",
            "c": "Para que uma empresa seja inovadora, deve gerar inovações radicais ao menos uma vez por ano.",
            "d": "Para que uma empresa seja inovadora, deve comprar novas tecnologias todos os anos e se atualizar de acordo com as demandas do mercado global.",
            "e": "Para que uma empresa seja inovadora, deve estar presente em parques tecnológicos de diferentes regiões do mundo."
        },
        "correta": "a",
        "explicacao": "Inovação envolve implementar novos produtos, processos gerenciais ou combinação de ambos, não necessariamente radicais ou presencia em parques tecnológicos."
    },
    # TEMA 6 - Papel dos serviços de consultoria para a inovação
    {
        "tema": 6,
        "pagina": 128,
        "texto": "Inovações podem envolver mudanças de equipamento, de recursos humanos, de métodos de trabalho ou uma combinação desses. De modo que existem duas possibilidades e linhas de análise para a inovação em produtos: produto tecnologicamente novo e produto tecnologicamente aprimorado. Com base nisso, o que pode ser considerada uma inovação radical?",
        "tipo": "mc",
        "opcoes": {
            "a": "É aquela em que o novo produto ou serviço incorpora novos elementos em relação ao anterior, sem que, no entanto, sejam alteradas suas funções básicas.",
            "b": "Trata-se de algo novo para o mercado e que traz uma grande mudança tecnológica, estrutural ou operacional.",
            "c": "São inovações que evitam que as empresas sejam surpreendidas pelos concorrentes.",
            "d": "É a inovação que tem como ponto de partida os referenciais estratégicos da empresa, ou seja, a sua missão, sua visão, seus valores e objetivos estratégicos.",
            "e": "É o tipo de inovação que tem a participação de multinacionais, governos de diferentes partes do mundo e vários investidores."
        },
        "correta": "b",
        "explicacao": "Inovação radical é algo novo para o mercado que traz grande mudança tecnológica, estrutural ou operacional."
    },
    {
        "tema": 6,
        "pagina": 128,
        "texto": "Inovação tecnológica é a implantação e a comercialização de um produto ou serviço com características aprimoradas, que favorecem, de forma significativa, os consumidores por meio de novas facilidades e possibilidade de uso. Com base nisso e nos demais estudos desta Unidade Curricular, assinale a alternativa que conceitua corretamente uma inovação incremental.",
        "tipo": "mc",
        "opcoes": {
            "a": "É aquela que consegue gerar incrementos reais à qualidade de vida das pessoas e organizações.",
            "b": "A inovação incremental é baseada na mobilização dos melhores pontos de vários produtos produzidos pela mesma empresa em determinado período.",
            "c": "Trata-se de um tipo de inovação praticada pelas mesmas empresas que geraram inovações radicais, pois somente elas podem lançar novas linhas de produtos de sua marca.",
            "d": "É aquela em que o novo produto ou serviço incorpora novos elementos em relação ao anterior, sem que, no entanto, sejam alteradas funções básicas.",
            "e": "É algo novo para o mercado e que traz uma grande mudança tecnológica, estrutural ou operacional."
        },
        "correta": "d",
        "explicacao": "Inovação incremental mantém as características principais do produto, com pequenos ajustes para melhoria de desempenho."
    },
    {
        "tema": 6,
        "pagina": 128,
        "texto": "O que pode ser considerada uma inovação de produto?",
        "tipo": "mc",
        "opcoes": {
            "a": "É a implantação e a comercialização de um produto com características aprimoradas, que favorecem, de forma significativa, os consumidores por meio de novas facilidades e possibilidade de uso.",
            "b": "É a adoção de métodos de produção novos ou significativamente melhorados, o que inclui métodos de entrega dos produtos. Podemos considerar a necessidade desse tipo de inovação para reduzir custos.",
            "c": "A inovação de produto é necessária para dar suporte e sustentação a um novo produto ou processo que será disponibilizado ao mercado ou à organização.",
            "d": "A inovação de produto é a transformação nos métodos de negócio da empresa. Pode ser uma mudança na organização do local do trabalho ou mesmo na relação com o mercado, os clientes e os fornecedores.",
            "e": "A inovação de produto é quando uma empresa lança algo significativamente novo e exporta toda sua produção inicial."
        },
        "correta": "a",
        "explicacao": "Inovação de produto consiste na implantação e comercialização de um bem com características aprimoradas, que favorecem os consumidores (Manual de Oslo)."
    }
]

def limpar_tela():
    # Para Termux/Unix/Windows
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def fazer_pergunta(q):
    print("\n" + "="*70)
    print(f"TEMA {q['tema']} | Página {q['pagina']}")
    print("="*70)
    print(q['texto'])
    print()
    
    if q['tipo'] == 'mc':
        for letra, texto in q['opcoes'].items():
            print(f"   {letra.upper()}) {texto}")
        print()
        while True:
            resp = input("Digite a letra da sua resposta (a, b, c, d, e): ").strip().lower()
            if resp in ['a','b','c','d','e']:
                break
            else:
                print("Opção inválida. Digite a, b, c, d ou e.")
        if resp == q['correta']:
            print("\n✅ CORRETO!")
        else:
            print(f"\n❌ ERRADO. A resposta correta é: {q['correta'].upper()}")
        print(f"\n📘 Explicação: {q['explicacao']}")
    else:  # pergunta aberta
        print("(Resposta dissertativa - não há correção automática)")
        print("Digite sua resposta abaixo (ou pressione Enter para ver a resposta esperada):")
        resp_user = input("Sua resposta: ").strip()
        print("\n📘 RESPOSTA ESPERADA (conforme o material didático):")
        print(f"{q['resposta_esperada']}")
        if resp_user:
            print("\nCompare sua resposta com a acima.")
        else:
            print("Use a resposta acima como referência para seus estudos.")
    
    input("\nPressione Enter para continuar...")

def main():
    print("="*70)
    print("   QUIZ - ATIVIDADES DE APRENDIZAGEM")
    print("   Curso Técnico em Agronegócio (SENAR)")
    print("   Módulo: Assessoria, Consultoria e Inovação")
    print("="*70)
    print(f"\nTotal de questões: {len(questoes)}")
    print("Este quiz contém todas as atividades dos Temas 1 a 6.\n")
    input("Pressione Enter para começar...")
    
    for i, q in enumerate(questoes, 1):
        limpar_tela()
        print(f"Questão {i} de {len(questoes)}")
        fazer_pergunta(q)
    
    limpar_tela()
    print("="*70)
    print("   PARABÉNS! Você concluiu todas as atividades.")
    print("   Revise o gabarito oficial no material didático.")
    print("="*70)

if __name__ == "__main__":
    main()
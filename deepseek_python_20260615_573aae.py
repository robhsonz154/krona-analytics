#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULADOR DE PREPARAÇÃO PARA PROVA - TEMA 1
Curso Técnico em Agronegócio (SENAR)
Módulo: Assessoria, Consultoria e Inovação no Agronegócio
Baseado fielmente no PDF (páginas 14 a 40)
"""

import random
import sys

# Banco de questões do TEMA 1, organizado por tópico e subtópico
# Estrutura: (pergunta, tipo, opcoes, correta, pagina, explicacao)
# tipo: 'mc' ou 'vf'

questoes_tema1 = [
    # ===================== TÓPICO 1.1 - CONCEITOS DE ASSESSORIA (p.16-19) =====================
    {
        "topico": "1.1 Conceitos de assessoria",
        "subt": "Papel do assessor",
        "pergunta": "Segundo Cruz (2008), qual é o papel do assessor na prestação de serviços técnicos gerenciais?",
        "tipo": "mc",
        "opcoes": {
            "a": "Agir como colaborador interno respondendo a demandas de superiores.",
            "b": "Elaborar estratégias e implementá-las sem consultar os donos da empresa.",
            "c": "Fazer um levantamento de estratégias diferentes de preparação e planejamento dos negócios, com foco na melhoria de produtividade e desempenho estratégico.",
            "d": "Manter a empresa atualizada sobre políticas públicas e cenários políticos.",
            "e": "Substituir o gestor da empresa na tomada de decisões operacionais."
        },
        "correta": "c",
        "pagina": "17",
        "explicacao": "Conforme a citação de Cruz (2008) na página 17: 'O papel do assessor é levantar estratégias diferentes de preparação e planejamento dos negócios, sempre com foco na melhoria da produtividade e em desempenho estratégico.'"
    },
    {
        "topico": "1.1 Conceitos de assessoria",
        "subt": "Características da assessoria",
        "pergunta": "A assessoria empresarial, diferentemente da consultoria, tem como característica principal:",
        "tipo": "mc",
        "opcoes": {
            "a": "Ser um serviço de curto prazo, com começo, meio e fim bem definidos.",
            "b": "Ser uma atividade sistemática de auxílio à empresa-cliente, podendo ser de longo prazo e com maior envolvimento no contexto interno.",
            "c": "Focar exclusivamente na implementação de softwares de gestão.",
            "d": "Ser prestada apenas por profissionais sem vínculo empregatício.",
            "e": "Não exigir diagnóstico da situação da empresa."
        },
        "correta": "b",
        "pagina": "18-19",
        "explicacao": "Na página 18-19, o material define: 'A assessoria empresarial é a atividade sistemática de auxiliar a empresa-cliente... [com] abordagem mais ampla do que a consultoria.' E no quadro comparativo: assessoria pode ser de longo prazo com mais envolvimento."
    },
    {
        "topico": "1.1 Conceitos de assessoria",
        "subt": "Relação assessor-cliente",
        "pergunta": "De acordo com o material, o assessor deve se destacar como um grande parceiro do cliente, caracterizando-se por:",
        "tipo": "mc",
        "opcoes": {
            "a": "Impor suas decisões sem considerar a opinião do cliente.",
            "b": "Agilidade nos processos, foco em soluções e forte comprometimento.",
            "c": "Manter distanciamento profissional para evitar conflitos de interesse.",
            "d": "Atuar apenas na gestão financeira da propriedade.",
            "e": "Substituir a mão de obra familiar na propriedade."
        },
        "correta": "b",
        "pagina": "18",
        "explicacao": "Na página 18: 'O assessor também deve se caracterizar pela agilidade nos processos, com foco em soluções e promover com seu cliente uma relação de forte comprometimento.'"
    },
    {
        "topico": "1.1 Conceitos de assessoria",
        "subt": "Conceito ampliado",
        "pergunta": "Verdadeiro ou Falso: Os serviços de assessoria no agronegócio englobam processos de produção, serviços gerenciais e organizacionais para empresas e instituições que se encontram antes, dentro e depois da porteira.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "17",
        "explicacao": "Página 17: 'No contexto do agronegócio, os serviços de assessoria estão cada vez mais amplos e completos. Hoje, englobam processos de produção, serviços gerenciais e organizacionais para empresas e instituições que se encontram antes, dentro e depois da porteira.'"
    },

    # ===================== TÓPICO 1.2 - CONCEITOS DE CONSULTORIA (p.20-29) =====================
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "Definição de consultoria",
        "pergunta": "Segundo Oliveira (2009), a consultoria pode ser conceituada como:",
        "tipo": "mc",
        "opcoes": {
            "a": "Um serviço permanente de gestão integrada à empresa.",
            "b": "Um processo interativo de um agente de mudanças externo à empresa, que auxilia nas tomadas de decisões sem controle direto da situação.",
            "c": "Uma relação empregatícia entre o consultor e a empresa contratante.",
            "d": "Um serviço gratuito oferecido pelo governo aos pequenos produtores.",
            "e": "Um método de fiscalização das atividades agropecuárias."
        },
        "correta": "b",
        "pagina": "20",
        "explicacao": "Página 20: 'Podemos conceituar a consultoria como um processo interativo de um agente de mudanças externo à empresa, o qual assume a responsabilidade de auxiliar os executivos e profissionais nas tomadas de decisões e não tem, entretanto, o controle direto da situação (OLIVEIRA, 2009).'"
    },
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "Vantagens da consultoria",
        "pergunta": "Oliveira (2009) apresenta três vantagens para empresas que utilizam serviços de consultoria. Quais são elas?",
        "tipo": "mc",
        "opcoes": {
            "a": "Redução de impostos, isenção fiscal e subsídios governamentais.",
            "b": "Crescimento do negócio, conhecimento sustentado e agilidade na aprendizagem.",
            "c": "Aumento da mão de obra, terceirização da produção e exportação.",
            "d": "Eliminação da concorrência, monopólio de mercado e fixação de preços.",
            "e": "Automação total, inteligência artificial e robotização."
        },
        "correta": "b",
        "pagina": "21-22",
        "explicacao": "Páginas 21-22: as três vantagens são: Crescimento do negócio, Conhecimento sustentado e Agilidade na aprendizagem."
    },
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "Causas da demanda por consultoria",
        "pergunta": "Dentre as causas que levam uma empresa a buscar serviços de consultoria, segundo Oliveira (2009), NÃO é citada:",
        "tipo": "mc",
        "opcoes": {
            "a": "Globalização.",
            "b": "Tecnologia.",
            "c": "Construção do futuro.",
            "d": "Responsabilidades ambientais e sociais.",
            "e": "Redução obrigatória de preços."
        },
        "correta": "e",
        "pagina": "23-25",
        "explicacao": "Nas páginas 23 a 25, as causas apresentadas são: Globalização (p.23), Tecnologia (p.24), Construção do futuro (p.24) e Responsabilidades ambientais e sociais (p.25). Não há menção a 'redução obrigatória de preços'."
    },
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "ESG",
        "pergunta": "O conceito ESG (environmental, social and governance) está relacionado a:",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas questões econômicas das empresas rurais.",
            "b": "Sustentabilidade ambiental, social e governança corporativa.",
            "c": "Tecnologias de irrigação de precisão.",
            "d": "Crédito rural e seguro agrícola.",
            "e": "Exportação de commodities."
        },
        "correta": "b",
        "pagina": "25",
        "explicacao": "Página 25: 'está surgindo um conceito muito importante, resumido pela sigla ESG – em inglês, environmental, social and governance –, que representa questões relativas à sustentabilidade ambiental, social e de governança corporativa nas empresas.'"
    },
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "Tipos de consultoria",
        "pergunta": "A consultoria que atua em um ou poucos assuntos dentro de uma área de conhecimento é chamada de:",
        "tipo": "mc",
        "opcoes": {
            "a": "Consultoria de pacote.",
            "b": "Consultoria artesanal.",
            "c": "Consultoria global.",
            "d": "Consultoria especializada.",
            "e": "Consultoria total."
        },
        "correta": "d",
        "pagina": "28",
        "explicacao": "Página 28: 'A consultoria especializada atua em um ou poucos assuntos dentro de uma área de conhecimento.'"
    },
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "Consultoria de pacote",
        "pergunta": "Verdadeiro ou Falso: Na consultoria de pacote, o serviço é prestado de forma padrão e previamente constituída, sem profundo conhecimento da realidade da empresa.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "27",
        "explicacao": "Página 27: 'Consultoria de pacote: Pode ser entendida como aquela prestada de forma padrão e previamente constituída, até mesmo sem profundo conhecimento da realidade da empresa.'"
    },
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "Consultoria artesanal",
        "pergunta": "Verdadeiro ou Falso: A consultoria artesanal preocupa-se em atender às necessidades do cliente por meio de um projeto baseado em metodologias especificamente estruturadas para a situação, sendo mais personalizada.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "27",
        "explicacao": "Página 27: 'Consultoria artesanal: Preocupa-se em atender às necessidades do cliente por meio de um projeto baseado em metodologias e técnicas administrativas especificamente estruturadas para a situação.'"
    },
    {
        "topico": "1.2 Conceitos de consultoria",
        "subt": "Vantagens e desvantagens do consultor interno",
        "pergunta": "Uma desvantagem do consultor interno (colaborador da própria empresa) em relação ao consultor externo é:",
        "tipo": "mc",
        "opcoes": {
            "a": "Maior conhecimento da informalidade nas relações interpessoais.",
            "b": "Maior acesso às pessoas e melhor interação.",
            "c": "Menor imparcialidade, pois não se arriscará tanto para manter o poder informal já conquistado.",
            "d": "Menor custo para a empresa.",
            "e": "Maior disponibilidade de horário."
        },
        "correta": "c",
        "pagina": "27",
        "explicacao": "Página 27, quadro 'Desvantagens': 'Não conta com um benefício importante de um modelo de consultoria externa relacionado ao risco: o profissional não se arriscará tanto, na tentativa de manter um poder informal já conquistado na empresa, o que indica que a imparcialidade ao longo do processo de consultoria poderá ser menor.'"
    },

    # ===================== TÓPICO 1.3 - APLICABILIDADE PARA O AGRONEGÓCIO (p.29-31) =====================
    {
        "topico": "1.3 Aplicabilidade no agronegócio",
        "subt": "Demandas dos produtores",
        "pergunta": "De acordo com pesquisa da CNA (2019), qual foi a principal demanda por melhorias apontada pelos produtores rurais?",
        "tipo": "mc",
        "opcoes": {
            "a": "Qualificação da mão de obra (36,1%)",
            "b": "Melhorias em infraestrutura e logística (40,9%)",
            "c": "Acesso ao crédito rural (59,9%)",
            "d": "Gestão dos custos de produção (49,7%)",
            "e": "Questões de gestão ambiental (35,2%)"
        },
        "correta": "c",
        "pagina": "31",
        "explicacao": "Página 31: 'as principais demandas por melhorias são: acesso ao crédito rural (59,9%), gestão dos custos de produção (49,7%), melhorias em infraestrutura e logística (40,9%)...'"
    },
    {
        "topico": "1.3 Aplicabilidade no agronegócio",
        "subt": "Campo de atuação",
        "pergunta": "Segundo o material, para o contexto de agricultores familiares, os serviços de assessoria e consultoria devem ser pensados principalmente:",
        "tipo": "mc",
        "opcoes": {
            "a": "Individualmente, para cada produtor.",
            "b": "Ao nível das cooperativas e associações que congregam vários produtores.",
            "c": "Apenas para os grandes produtores de soja.",
            "d": "Exclusivamente pelo poder público.",
            "e": "Por meio de consultorias internacionais."
        },
        "correta": "b",
        "pagina": "30",
        "explicacao": "Página 30: 'Para o contexto de agricultores familiares, os serviços de assessoria e consultoria devem ser pensados ao nível das cooperativas e associações que congregam vários produtores, por exemplo.'"
    },

    # ===================== TÓPICO 2 - INOVAÇÃO E TRANSFERÊNCIA DE TECNOLOGIA (p.32-40) =====================
    {
        "topico": "2. Inovação e transferência de tecnologia",
        "subt": "Conceito de inovação",
        "pergunta": "De acordo com Bellaver (2005), inovação pode ser definida como:",
        "tipo": "mc",
        "opcoes": {
            "a": "Apenas a invenção de novos produtos.",
            "b": "Uma nova ideia implementada com sucesso, que produz resultados econômicos.",
            "c": "Qualquer mudança no processo produtivo, mesmo que sem resultados.",
            "d": "A aquisição de máquinas e equipamentos importados.",
            "e": "A redução de custos a qualquer preço."
        },
        "correta": "b",
        "pagina": "35",
        "explicacao": "Página 35: Bellaver (2005) oferece definições: 'Inovação é uma nova ideia implementada com sucesso, que produz resultados econômicos.'"
    },
    {
        "topico": "2. Inovação e transferência de tecnologia",
        "subt": "Exemplo de inovação na pecuária",
        "pergunta": "Segundo a Embrapa (2016), qual técnica é usada para acelerar a produção de bezerros geneticamente superiores, reduzindo o tempo de melhoramento genético de 10 anos para menos?",
        "tipo": "mc",
        "opcoes": {
            "a": "Inseminação artificial (IA)",
            "b": "Inseminação artificial em tempo fixo (IATF)",
            "c": "Transferência de embriões (TE)",
            "d": "Fertilização in vitro (FIV)",
            "e": "Clonagem reprodutiva"
        },
        "correta": "d",
        "pagina": "36",
        "explicacao": "Página 36: 'A fertilização in vitro (FIV) é usada para acelerar a produção de bezerros e, consequentemente, de bovinos geneticamente superiores.'"
    },
    {
        "topico": "2. Inovação e transferência de tecnologia",
        "subt": "Transferência de tecnologia",
        "pergunta": "A transferência de tecnologia pode ser caracterizada como:",
        "tipo": "mc",
        "opcoes": {
            "a": "Uma troca de informações entre um provedor e um receptor.",
            "b": "A venda de patentes para empresas estrangeiras.",
            "c": "Um processo burocrático de registro de propriedade intelectual.",
            "d": "Uma obrigação legal de todos os produtores rurais.",
            "e": "Apenas a importação de máquinas agrícolas."
        },
        "correta": "a",
        "pagina": "37",
        "explicacao": "Página 37: 'A transferência de tecnologia pode ser caracterizada como uma troca de informações entre um provedor (como a Embrapa ou a universidade) e um receptor (pecuarista que passou a utilizar a técnica FIV, por exemplo).'"
    },
    {
        "topico": "2. Inovação e transferência de tecnologia",
        "subt": "Desafios da inovação no agro",
        "pergunta": "Segundo o material, por que o caminho entre o provedor e o receptor de tecnologia é extremamente complexo?",
        "tipo": "mc",
        "opcoes": {
            "a": "Porque o governo não regulamenta a transferência.",
            "b": "Porque o público dos produtores rurais é extremamente rigoroso e conservador, preferindo evitar riscos.",
            "c": "Porque faltam universidades e centros de pesquisa no Brasil.",
            "d": "Porque a legislação ambiental proíbe novas tecnologias.",
            "e": "Porque os consultores não estão preparados."
        },
        "correta": "b",
        "pagina": "37",
        "explicacao": "Página 37: 'O público dos produtores rurais é extremamente rigoroso e conservador, ou seja, muitas vezes prefere manter-se um ambiente mais controlado e sem exposição aos riscos que a implementação de uma nova tecnologia inevitavelmente comporta.'"
    },
    {
        "topico": "2. Inovação e transferência de tecnologia",
        "subt": "Cadeia inovadora",
        "pergunta": "O estudo de Alves et al. (2006) constatou que qual cadeia produtiva no Brasil é essencialmente inovadora e está entre as mais competitivas do mundo?",
        "tipo": "mc",
        "opcoes": {
            "a": "Cadeia do café",
            "b": "Cadeia da soja",
            "c": "Cadeia da avicultura",
            "d": "Cadeia da cana-de-açúcar",
            "e": "Cadeia da bovinocultura de corte"
        },
        "correta": "c",
        "pagina": "37",
        "explicacao": "Página 37: 'Um estudo conduzido por Alves et al. (2006) constatou que a cadeia produtiva da avicultura no Brasil é essencialmente inovadora e, por isso, alcançou resultados positivos ao longo dos anos e está entre as mais competitivas do mundo todo.'"
    },
    {
        "topico": "2. Inovação e transferência de tecnologia",
        "subt": "Papel dos assessores e consultores na inovação",
        "pergunta": "Verdadeiro ou Falso: Os prestadores de serviços de assessoria e consultoria são verdadeiros agentes que direcionam e viabilizam a transferência de tecnologias para os produtores rurais.",
        "tipo": "vf",
        "correta": "V",
        "pagina": "37",
        "explicacao": "Página 37: 'Outro ponto essencial para que a inovação no agronegócio seja uma constante é considerar que os prestadores de serviços de assessoria e consultoria são verdadeiros agentes que direcionam e viabilizam a transferência de tecnologias.'"
    }
]

def limpar_tela():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def mostrar_resultado(acertos, total):
    print("\n" + "="*70)
    print("   RESULTADO FINAL DO SIMULADOR (TEMA 1)")
    print("="*70)
    print(f"Total de questões: {total}")
    print(f"Acertos: {acertos}")
    print(f"Percentual: {acertos/total*100:.1f}%")
    if acertos/total >= 0.7:
        print("\n🎉 PARABÉNS! Você está preparado para a prova do TEMA 1.")
    elif acertos/total >= 0.5:
        print("\n📚 Bom desempenho! Revise os tópicos onde errou e tente novamente.")
    else:
        print("\n⚠️ Sugerimos revisar o material didático (páginas 14 a 40) antes da prova.")
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
    print("   TEMA 1: CONCEITOS BÁSICOS DE ASSESSORIA E CONSULTORIA")
    print("="*70)
    print(f"\nEste simulador contém {len(questoes_tema1)} questões")
    print("cobrindo todos os tópicos e subtópicos do Tema 1 (páginas 14 a 40).")
    print("\nAs questões podem ser de múltipla escolha (A,B,C,D,E) ou Verdadeiro/Falso (V/F).")
    print("Ao final, você receberá seu percentual de acertos.\n")
    input("Pressione Enter para iniciar...")
    
    # Embaralhar questões para maior desafio
    questoes = random.sample(questoes_tema1, len(questoes_tema1))
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
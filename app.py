import streamlit as st

st.set_page_config(page_title="Benessere saúde integral", page_icon="🩺", layout="wide")

# Dicionário de serviços (valores atualizados e organizados)
servicos = {
    # Profissionais
    "Dra. Karol": 500.00,
    "Dr. Gabriel": 600.00,
    "Nutricionista": 300.00,
    "Bioimpedância": 120.00,

    # Testes
    "Teste Intestinal": 1600.00,
    "Teste de Sensibilidade Alimentar": 1800.00,

    # Implantes hormonais
    "Implante - Menopausa": 3200.00,
    "Implante - Testosterona": 2800.00,
    "Implante - Gestrinona": 0.00,
    "Implante - Outros": 0.00,

    # Implanon
    "Implanon - Colocação": 2100.00,
    "Implanon - Retirada com troca": 300.00,
    "Implanon - Retirada isolada (Consulta + 200)": 0.00,

    # DIU
    "DIU - Colocação Hormonal": 950.00,
    "DIU - Colocação Não Hormonal": 750.00,
    "DIU - Retirada": 200.00,

    # Vitaminas e terapias
    "Vitamina D": 140.00,
    "Vitamina B12 (500/2500)": 140.00,
    "Complexo B": 140.00,
    "Coenzima Q10": 140.00,
    "M. Complex / S. Complex (Ativador metabólico)": 140.00,
    "Vitamina C (soro)": 300.00,
    "Vitamina C + Complexo B (soro)": 380.00,

    # Ferro
    "Ferro (soro) - 1 ampola": 250.00,
    "Ferro (soro) - 2 ampolas": 400.00,

    # Cirurgias e procedimentos
    "Cirurgia I": 600.00,
    "Cirurgia II": 1000.00,
    "Cirurgia III": 1500.00,
    "Retirada de pólipos": 300.00,
    "Cauterização elétrica": 600.00,
    "Cauterização com ATA": 150.00,
    "Drenagens": 400.00,
}

# Mensagens de pós-consulta
consultas_mensagens = {
    "Consulta com Dra. Karol": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para saber como você está se sentindo após a consulta.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Consulta com Dr. Gabriel": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nO Dr. Gabriel pediu para saber como você está se sentindo após a consulta.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Consulta com Nutricionista": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nNossa nutricionista pediu para saber como você está se sentindo após a consulta.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Revisão de Exames": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nPassando para confirmar se ficou tudo claro após a revisão dos seus exames.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Retorno Geral": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nSó passando pra saber como você está após o seu retorno.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
}

procedimentos_mensagens = {
    "Colocação de Implanon": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para acompanhar como você está se sentindo após a colocação do Implanon.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Retirada de Implanon": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para saber como você está após a retirada do Implanon.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Colocação de DIU": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para saber como você está se sentindo após a colocação do DIU.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Retirada de DIU": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para saber como você está após a retirada do DIU.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Vitaminas ou Soros": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nPassando pra saber como você está se sentindo após a aplicação das vitaminas/soro.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Implante Hormonal": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para saber como você está se sentindo após o implante hormonal.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Cauterização": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para acompanhar como você está após a cauterização.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
    "Retirada de Pólipos ou Cirurgia": "Oi [Nome], tudo bem? Aqui é a Isabela da Benessere!\nA Dra. Karol pediu para saber como você está se sentindo após o procedimento.\nSe precisar de algo ou tiver dúvidas, estou à disposição!",
}

# Links de avaliação
avaliacoes_links = {
    "Dra. Karol": "https://g.page/r/CW4RmAUUq1Q5EAE/review",
    "Dr. Gabriel": "https://g.page/r/Ce1HPhS5Y8RaEBM/review"
}

# Funções para exibir as páginas
def exibir_procedimentos():
    st.header("📋 Tabela de Valores do Consultório")
    st.markdown("### 👩‍⚕️ Consultas e Exames de Avaliação")
    st.write(f"- **Dra. Karol**: R$ {servicos['Dra. Karol']:.2f}")
    st.write(f"- **Dr. Gabriel**: R$ {servicos['Dr. Gabriel']:.2f}")
    st.write(f"- **Nutricionista**: R$ {servicos['Nutricionista']:.2f}")
    st.write(f"- **Bioimpedância**: R$ {servicos['Bioimpedância']:.2f}")

    st.markdown("### 💉 Implanon")
    st.markdown("""
- Colocação: R$ 2.100,00  
- Retirada com troca: R$ 300,00  
- Retirada isolada (consulta + R$ 200,00)  
🔹 Exige teste de gravidez
""")

    st.markdown("### 🧬 DIU")
    st.markdown("""
- Colocação Hormonal: R$ 950,00  
- Colocação Não Hormonal: R$ 750,00  
- Retirada: R$ 200,00  
🔹 Exige teste de gravidez
""")

    st.markdown("### 🌼 Implantes Hormonais")
    st.markdown("""
- Menopausa: R$ 3.200,00  
- Testosterona: R$ 2.800,00  
- Gestrinona: Valor a informar  
- Outros: Preencher manualmente
""")

    st.markdown("### 🛠️ Cirurgias e Procedimentos")
    st.markdown("""
- Cirurgia I: R$ 600,00  
- Cirurgia II: R$ 1.000,00  
- Cirurgia III: R$ 1.500,00  
- Retirada de pólipos: R$ 300,00  
- Cauterização elétrica: R$ 600,00  
- Cauterização com ATA: R$ 150,00 por sessão  
- Drenagens: R$ 400,00
""")

    st.markdown("### 🧪 Testes")
    st.markdown("""
- Teste Intestinal: R$ 1.600,00  
- Teste de Sensibilidade Alimentar: R$ 1.800,00
""")

    st.markdown("### 💊 Vitaminas e Suplementos")
    st.markdown("""
- Vitamina D: R$ 140,00  
- Vitamina B12 (500/2500): R$ 140,00  
- Complexo B: R$ 140,00  
- Coenzima Q10: R$ 140,00  
- M. Complex / S. Complex (Ativador metabólico): R$ 140,00  
- Vitamina C (soro): R$ 300,00  
- Vitamina C + Complexo B (soro): R$ 380,00
""")

    st.markdown("### 🩸 Ferro (Soro)")
    st.markdown("""
Para pessoas com deficiência de absorção:  
- 1 ampola: R$ 250,00  
- 2 ampolas: R$ 400,00
""")

def exibir_mensagens():
    st.header("💬 Mensagens de Pós-Consulta")
    tipo = st.radio("Selecione o tipo de mensagem:", ("Consultas", "Procedimentos"))

    if tipo == "Consultas":
        opcao = st.selectbox("Escolha a mensagem:", list(consultas_mensagens.keys()))
        nome = st.text_input("Nome do paciente:")
        mensagem = consultas_mensagens[opcao].replace("[Nome]", nome if nome else "[Nome]")
        st.text_area("Mensagem", value=mensagem, height=200)

    else:
        opcao = st.selectbox("Escolha a mensagem:", list(procedimentos_mensagens.keys()))
        nome = st.text_input("Nome do paciente:")
        mensagem = procedimentos_mensagens[opcao].replace("[Nome]", nome if nome else "[Nome]")
        st.text_area("Mensagem", value=mensagem, height=200)

def exibir_mensagens_avaliacao():
    st.header("💬 Mensagens de Avaliação no WhatsApp")
    profissional = st.selectbox("Selecione o profissional:", list(avaliacoes_links.keys()))
    nome_paciente = st.text_input("Nome do paciente:")

    if profissional == "Dra. Karol":
        mensagem = f"""Oi {nome_paciente}! Que bom saber que está tudo bem! 
Se puder deixar uma avaliação para a Dra. Karol, ficaremos muito felizes. 
Isso nos ajuda a continuar oferecendo o melhor atendimento! 

É só clicar aqui: {avaliacoes_links['Dra. Karol']}

Obrigada pelo carinho e confiança! Estou sempre à disposição."""
    else:
        mensagem = f"""Oi {nome_paciente}! Fico feliz em saber que deu tudo certo! 
Se puder deixar uma avaliação para o Dr. Gabriel, seria ótimo. 
Seu feedback é muito importante para nós! 

É só clicar aqui: {avaliacoes_links['Dr. Gabriel']}

Muito obrigada! Seguimos à disposição para o que precisar."""

    st.text_area("Mensagem para WhatsApp", value=mensagem, height=250)

# Menu
pagina = st.sidebar.selectbox("Navegue pelas páginas", [
    "🏠 Início",
    "📋 Tabela de Valores",
    "💬 Mensagens de Pós-Consulta",
    "💬 Mensagens de Avaliação"
])

if pagina == "🏠 Início":
    st.title("🩺 Tabela de Valores - Consultório Médico")
    st.write("Bem-vinda! Consulte os valores organizados por categorias no menu lateral.")

elif pagina == "📋 Tabela de Valores":
    exibir_procedimentos()

elif pagina == "💬 Mensagens de Pós-Consulta":
    exibir_mensagens()

elif pagina == "💬 Mensagens de Avaliação":
    exibir_mensagens_avaliacao()

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

# Página de exibição de valores
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
ℹ️ Exige teste de gravidez
""")

    st.markdown("### 🧬 DIU")
    st.markdown("""
- Colocação Hormonal: R$ 950,00  
- Colocação Não Hormonal: R$ 750,00  
- Retirada: R$ 200,00  
ℹ️ Exige teste de gravidez
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

# Menu
pagina = st.sidebar.selectbox("Navegue pelas páginas", [
    "🏠 Início",
    "📋 Tabela de Valores"
])

if pagina == "🏠 Início":
    st.title("🩺 Tabela de Valores - Consultório Médico")
    st.write("Bem-vinda! Consulte os valores organizados por categorias no menu lateral.")

elif pagina == "📋 Tabela de Valores":
    exibir_procedimentos()
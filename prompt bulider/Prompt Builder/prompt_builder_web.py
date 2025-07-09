import streamlit as st
import textwrap

# --- Configuração da Página Streamlit ---
st.set_page_config(
    page_title="Montador de Prompt VEO3 (Web)",
    page_icon="🎥", # Um emoji como ícone da aba do navegador
    layout="wide" # Ocupa a largura total da tela, o que é ótimo para abas e muitos elementos
)

# --- Definição dos Dados do Aplicativo ---
sections_data = {
    "Alma do Vídeo": {
        "description": "Defina a ideia principal, o gênero e o sentimento que você quer transmitir. \n*Lembre-se: Para campos de texto livre, digite em inglês para um prompt mais eficaz.*",
        "checkboxes": {
            "Objetivo/Gênero": [
                ("Comercial", "Commercial"), ("Narrativa", "Narrative"), ("Educacional", "Educational"), ("Vídeo Conceitual", "Concept Video"),
                ("Vídeo Musical", "Music Video"), ("Estilo Documental", "Documentary Style"), ("Curta-metragem", "Short Film"), ("Vídeo em Loop", "Looping Video")
            ],
            "Emoção/Sentimento": [
                ("Épico", "Epic"), ("Misterioso", "Mysterious"), ("Alegre", "Joyful"), ("Calmo", "Calm"), ("Intenso", "Intense"),
                ("Inspirador", "Inspirational"), ("Caótico", "Chaotic"), ("Nostálgico", "Nostalgic"), ("Onírico", "Dreamlike")
            ]
        },
        "text_inputs": {
            "Ideia Central (Frase Curta) - *DIGITE EM INGLÊS* (e.g., A cat playing with yarn)": {"key": "Idea Central", "required": True}
        }
    },
    "Universo Visual": {
        "description": "Configure o palco da sua cena, incluindo o local, a hora e o clima.",
        "checkboxes": {
            "Localização": [
                ("Urbano", "Urban"), ("Floresta", "Forest"), ("Montanha", "Mountain"), ("Espaço", "Space"), ("Subaquático", "Underwater"),
                ("Castelo", "Castle"), ("Cidade Cyberpunk", "Cyberpunk City"), ("Quarto Aconchegante", "Cozy Room"), ("Local Industrial", "Industrial Site")
            ],
            "Hora do Dia / Iluminação": [
                ("Amanhecer", "Sunrise"), ("Pôr do Sol / Hora Dourada", "Sunset / Golden Hour"), ("Noite / Céu Estrelado / Luar", "Night / Starry Sky / Moonlight"),
                ("Iluminação Dramática", "Dramatic Lighting"), ("Luz Suave", "Soft Light"), ("Luzes Neon", "Neon Lights"), ("Luz de Velas", "Candlelight"), ("Iluminação Volumétrica", "Volumetric Lighting")
            ],
            "Atmosfera / Clima": [
                ("Chuvoso", "Rainy"), ("Nevando", "Snowy"), ("Nebuloso", "Foggy"), ("Ventoso", "Windy"), ("Brilhante", "Bright"), ("Sombrio", "Gloomy"),
                ("Pacífico", "Peaceful"), ("Tempestuoso", "Stormy"), ("Antigo", "Ancient"), ("Futurista", "Futuristic"), ("Mágico", "Magical")
            ]
        },
        "text_inputs": {
            "Localização Específica (Opcional) - *DIGITE EM INGLÊS* (e.g., Golden Gate Bridge)": {"key": "Specific Location", "required": False},
            "Detalhes de Iluminação Adicionais (Opcional) - *DIGITE EM INGLÊS* (e.g., Sunlight filtering through leaves)": {"key": "Additional Lighting Details", "required": False}
        }
    },
    "Protagonistas": {
        "description": "Detalhe os principais elementos visuais (pessoas, objetos, criaturas).",
        "checkboxes": {
            "Tipo Principal": [
                ("Homem", "Man"), ("Mulher", "Woman"), ("Criança", "Child"), ("Idoso", "Elderly Person"), ("Cachorro", "Dog"), ("Gato", "Cat"), ("Lobo", "Wolf"), ("Águia", "Eagle"),
                ("Dragão", "Dragon"), ("Unicórnio", "Unicorn"), ("Robô", "Robot"), ("Androide", "Android"), ("Drone", "Drone"),
                ("Carro", "Car"), ("Nave Espacial", "Spaceship"), ("Espada", "Sword"), ("Livro", "Book"), ("Bola de Cristal", "Crystal Ball"), ("Artefato Antigo", "Ancient Artifact"),
                ("Forma Abstrata", "Abstract Shape"), ("Enxame de Partículas", "Particle Swarm")
            ],
             "Estado / Ação Primária (Inicial) - Se aplicável": [
                ("Parado", "Standing Still"), ("Sentado", "Sitting"), ("Deitado", "Lying Down"), ("Em Movimento", "Moving"),
                ("Brilhando", "Glowing"), ("Saindo Fumaça", "Smoking"), ("Quebrado", "Broken"), ("Transformando", "Transforming"), ("Sorrindo", "Smiling"), ("Franzindo a testa", "Frowning"), ("Determinado", "Determined"), ("Assustado", "Afraid")
            ]
        },
        "text_inputs": {
            "Características da Aparência (e.g., Black and white cat, Green eyes) - *DIGITE EM INGLÊS*": {"key": "Appearance Characteristics", "required": False},
            "Tipo Específico (Se não estiver na lista - e.g., Giraffe, Tank) - *DIGITE EM INGLÊS*": {"key": "Specific Type", "required": False}
        }
    },
    "Coreografia": {
        "description": "Defina o que acontece na cena e como a 'câmera' se move.",
        "checkboxes": {
            "Ações dos Sujeitos": [
                ("Correndo", "Running"), ("Voando", "Flying"), ("Nadando", "Swimming"), ("Saltando", "Jumping"), ("Caindo", "Falling"), ("Subindo", "Rising"),
                ("Transformando", "Transforming"), ("Dissolvendo", "Dissolving"), ("Aparecendo", "Appearing"), ("Lutando", "Fighting"), ("Dançando", "Dancing"), ("Meditando", "Meditating"), ("Interagindo", "Interacting")
            ],
            "Movimento de Câmera (Escolha um ou mais)": [
                ("Câmera Fixa", "Static Shot"), ("Panorâmica Lenta Esquerda", "Slow Pan Left"), ("Panorâmica Lenta Direita", "Slow Pan Right"), ("Inclinação Rápida Cima", "Fast Tilt Up"), ("Inclinação Rápida Baixo", "Fast Tilt Down"),
                ("Travelling Suave Frente", "Smooth Dolly Forward"), ("Travelling Suave Trás", "Smooth Dolly Backward"), ("Câmera Acompanhando", "Tracking Shot"),
                ("Câmera Elevada Descendo", "Crane Shot Descending"), ("Câmera Elevada Subindo", "Crane Shot Ascending"), ("Câmera Orbitando", "Orbiting Camera"),
                ("Efeito Câmera na Mão", "Handheld Camera Effect"), ("Zoom In", "Zoom In"), ("Zoom Out", "Zoom Out")
            ],
            "Plano / Enquadramento Inicial": [
                ("Plano Geral Extremo", "Extreme Wide Shot"), ("Plano Geral", "Wide Shot"), ("Plano Médio", "Medium Shot"),
                ("Plano Fechado", "Close-Up"), ("Plano Detalhe", "Extreme Close-Up"), ("Vista em Primeira Pessoa", "First-Person View"),
                ("Vista Aérea", "Bird's Eye View"), ("Plano de Baixo Ângulo", "Low Angle Shot")
            ]
        },
         "text_inputs": {
            "Ação Específica Adicional (Opcional) - *DIGITE EM INGLÊS* (e.g., Character opens a mystical book)": {"key": "Specific Action", "required": False},
            "Detalhes de Movimento de Câmera (e.g., Zoom In to the eye) - *DIGITE EM INGLÊS*": {"key": "Camera Movement Details", "required": False},
            "Sujeito para Orbitar (se 'Câmera Orbitando' selecionado) - *DIGITE EM INGLÊS*": {"key": "Subject to Orbit", "required": False}
         }
    },
    "Assinatura Artística": {
        "description": "Escolha o estilo visual, paleta de cores e qualidade técnica. Ouse ser original!",
        "checkboxes": {
            "Estilo Artístico": [
                ("Fotorrealista", "Photorealistic"), ("Cinematográfico", "Cinematic"), ("Cena de Filme de Alto Orçamento", "High-Budget Film Still"), ("Estilo Anime", "Anime Style"), ("Estilo Cartoon", "Cartoon Style"),
                ("Estilo Pintura a Óleo", "Oil Painting Style"), ("Estilo Aquarela", "Watercolor Style"), ("Pixel Art", "Pixel Art"), ("Voxel Art", "Voxel Art"), ("Abstrato Geométrico", "Abstract Geometric"),
                ("Surreal", "Surreal"), ("Onírico", "Dreamlike"), ("Cyberpunk", "Cyberpunk"), ("Steampunk", "Steampunk"), ("Dieselpunk", "Dieselpunk"),
                ("Arte Fantástica", "Fantasy Art"), ("Arte de Ficção Científica", "Sci-Fi Art"), ("Estilo Noir", "Noir Style"), ("Efeitos Visuais (VFX)", "VFX")
            ],
            "Paleta de Cores / Atmosfera Visual": [
                ("Cores Vibrantes", "Vibrant Colors"), ("Paleta Suave", "Muted Palette"), ("Monocromático", "Monochromatic"), ("Preto e Branco", "Black and White"),
                ("Tons Dourados", "Golden Tones"), ("Tons Frios", "Cool Tones"), ("Tons Quentes", "Warm Tones"), ("Cores Pastel", "Pastel Colors")
            ],
            "Qualidade / Efeitos Visuais": [
                ("Alta Definição", "High Definition"), ("4K", "4K"), ("8K", "8K"), ("Alto Detalhe", "High Detail"), ("Foco Nítido", "Sharp Focus"),
                ("Grão de Filme", "Film Grain Effect"), ("Efeito Bokeh", "Bokeh Effect"), ("Lens Flare", "Lens Flare"), ("Sombras Dramáticas", "Dramatic Shadows"),
                ("Animação Suave", "Smooth Animation")
            ]
        },
        "text_inputs": {
            "Estilo Específico ou Referência (e.g., in the style of Salvador Dalí, similar to Blade Runner movie) - *DIGITE EM INGLÊS*": {"key": "Specific Style/Reference", "required": False},
            "Paleta de Cores Específica Adicional (Opcional) - *DIGITE EM INGLÊS*": {"key": "Additional Color Palette", "required": False},
            "Efeitos Visuais Adicionais (Opcional) - *DIGITE EM INGLÊS*": {"key": "Additional Visual Effects", "required": False}
        }
    },
    "Parâmetros Técnicos": {
        "description": "Defina as configurações técnicas como formato, duração, velocidade e elementos a excluir (prompt negativo).",
        "checkboxes": {
             "Velocidade / Ritmo": [
                ("Velocidade Normal", "Normal Speed"), ("Câmera Rápida (Time-Lapse)", "Time-Lapse"), ("Câmera Lenta (Slow Motion)", "Slow Motion"), ("Ritmo Rápido", "Fast-Paced"), ("Ritmo Lento", "Slow-Paced")
            ],
            "Loop": [("Vídeo em Loop Contínuo", "Seamless Loop")]
        },
         "text_inputs": {
            "Formato / Proporção (e.g., Horizontal 16:9, Vertical 9:16, Square 1:1) - *DIGITE EM INGLÊS*": {"key": "Format / Aspect Ratio", "required": False},
            "Duração Aproximada em Segundos (e.g., 10s)": {"key": "Approximate Duration", "required": False},
            "Prompt Negativo (o que NÃO deve aparecer - *DIGITE EM INGLÊS*)": {"key": "Negative Prompt", "required": False} # Campo para Prompt Negativo
         }
    }
}

# --- Título Principal do Aplicativo ---
st.title("�� Montador de Prompt para Vídeo VEO3 (Web)")
st.markdown("Bem-vindo, Caio! Crie prompts poderosos para seus vídeos IA. ✨")

# --- Inicializa st.session_state para guardar os valores ---
if 'generated_prompt' not in st.session_state:
    st.session_state.generated_prompt = ""
if 'partial_prompt' not in st.session_state:
    st.session_state.partial_prompt = ""
if 'required_fields_missing' not in st.session_state:
    st.session_state.required_fields_missing = False


# A função 'clear_all_inputs' foi removida, pois o botão não existe mais.

# --- Construção das Abas com st.tabs() ---
tab_titles = list(sections_data.keys())
tabs = st.tabs(tab_titles)

all_selected_keywords = {}
all_text_inputs = {}
required_fields_filled = {}

for i, tab_name in enumerate(tab_titles):
    with tabs[i]:
        data = sections_data[tab_name]
        st.markdown(f"**_{data['description']}_**")

        # --- Seções de Checkboxes ---
        if "checkboxes" in data:
            for section_title, keywords_list in data["checkboxes"].items():
                st.subheader(section_title)
                cols = st.columns(3)
                col_idx = 0

                for pt_label, en_keyword in keywords_list:
                    checkbox_key = f"checkbox_{tab_name}_{section_title}_{en_keyword}"

                    with cols[col_idx]:
                        selected = st.checkbox(pt_label, key=checkbox_key)
                        if selected:
                            if tab_name not in all_selected_keywords:
                                all_selected_keywords[tab_name] = []
                            all_selected_keywords[tab_name].append(en_keyword)
                    col_idx = (col_idx + 1) % 3

        # --- Campos de Texto ---
        if "text_inputs" in data:
            for input_label, input_config in data["text_inputs"].items():
                input_key = f"text_input_{tab_name}_{input_config['key']}"

                current_value = st.text_input(input_label, key=input_key)
                all_text_inputs[input_config['key']] = current_value.strip()

                if input_config.get("required", False) and not current_value.strip():
                    required_fields_filled[input_config['key']] = False
                else:
                    required_fields_filled[input_config['key']] = True

# --- Geração e Exibição do Prompt Parcial (Atualização em Tempo Real) ---
partial_prompt_parts_list = []
for tab_name, data_tab in sections_data.items():
    section_parts = []

    for input_label, input_config in data_tab.get("text_inputs", {}).items():
        key_in_prompt = input_config["key"]
        text_value = all_text_inputs.get(key_in_prompt, "").strip()
        if text_value and key_in_prompt != "Negative Prompt":
            section_parts.append(f"{key_in_prompt}: {text_value}")

    if tab_name in all_selected_keywords:
        if all_selected_keywords[tab_name]:
            section_parts.append(f"Keywords: {', '.join(all_selected_keywords[tab_name])}")

    if section_parts:
        partial_prompt_parts_list.append(f"[{tab_name}]: " + " | ".join(section_parts))

st.session_state.partial_prompt = textwrap.fill(" | ".join(partial_prompt_parts_list), width=100)

st.subheader("Prompt Parcial (Atualização em tempo real):")
st.text_area("partial_prompt_display", value=st.session_state.partial_prompt, height=100, disabled=True)

# --- Botões de Ação: Gerar ---
st.subheader("Ações:")
col_buttons = st.columns(1) # Cria uma única coluna

with col_buttons[0]: # Usa a primeira (e única) coluna
    if st.button("✨ Gerar Prompt Completo", use_container_width=True):
        is_missing = False
        for field_key, is_filled in required_fields_filled.items():
            if not is_filled:
                st.error(f"Por favor, preencha o campo obrigatório: '{field_key}'")
                is_missing = True
                break

        if is_missing:
            st.session_state.required_fields_missing = True
            st.session_state.generated_prompt = "Preencha todos os campos obrigatórios para gerar o prompt."
        else:
            st.session_state.required_fields_missing = False
            full_prompt_parts = []
            negative_prompt_parts = []

            for tab_name, data_tab in sections_data.items():
                section_parts_for_prompt = []

                for input_label, input_config in data_tab.get("text_inputs", {}).items():
                    key_in_prompt = input_config["key"]
                    text_value = all_text_inputs.get(key_in_prompt, "").strip()
                    if text_value:
                        if key_in_prompt == "Negative Prompt":
                            negative_prompt_parts.append(text_value)
                        else:
                            section_parts_for_prompt.append(text_value)

                if tab_name in all_selected_keywords:
                    if all_selected_keywords[tab_name]:
                        section_parts_for_prompt.extend(all_selected_keywords[tab_name])

                if section_parts_for_prompt:
                    full_prompt_parts.append(", ".join(section_parts_for_prompt))

            final_prompt = ", ".join(full_prompt_parts)

            if negative_prompt_parts:
                final_prompt += " | Negative Prompt: " + ", ".join(negative_prompt_parts)

            st.session_state.generated_prompt = textwrap.fill(final_prompt, width=100)

# O bloco do botão "Limpar Tudo" foi completamente removido, e a função clear_all_inputs também.


# --- Exibição do Prompt Completo ---
st.subheader("Prompt Completo (Pronto para copiar para o VEO3):")
st.text_area("full_prompt_display", value=st.session_state.generated_prompt, height=150)

if st.session_state.generated_prompt:
    st.info("Para copiar o prompt, selecione o texto acima e use Ctrl+C (ou Cmd+C no Mac).")

# Para rodar, salve este código como 'prompt_builder_web.py' e no terminal, execute:
# python -m streamlit run prompt_builder_web.py
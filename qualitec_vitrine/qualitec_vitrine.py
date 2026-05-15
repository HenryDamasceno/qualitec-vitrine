import reflex as rx

# Cores do tema (Industrial/Premium)
primary_color = "#00AEEF" #logo Qualitec)
dark_bg = "#0F172A"
card_bg = "#1E293B"

def navbar():
    return rx.hstack(
        # Logo da empresa
        rx.link(
            rx.image(
                src="/logo_final_3.png", 
                height="60px", 
                object_fit="contain",
                margin="0",
                padding="0"
            ),
            href="/",
        ),
        rx.spacer(),
        rx.hstack(
            rx.link("Sobre", href="#sobre", color="white", _hover={"color": primary_color}),
            rx.link("Serviços", href="#servicos", color="white", _hover={"color": primary_color}),
            rx.link("Portfólio", href="#portfolio", color="white", _hover={"color": primary_color}),
            rx.link("Clientes", href="#clientes", color="white", _hover={"color": primary_color}),
            rx.link("Contato", href="#contato", color="white", _hover={"color": primary_color}),
            spacing="4",
            display=["none", "none", "flex"] # Oculto em telas muito pequenas (mobile)
        ),
        position="fixed",
        top="0",
        width="100%",
        z_index="100",
        background_color="rgba(15, 23, 42, 0.9)",
        backdrop_filter="blur(10px)",
        padding_x="2em",
        padding_y="1em",
        align_items="center",
        border_bottom=f"1px solid {card_bg}"
    )

def hero_section():
    return rx.box(
        rx.vstack(
            rx.heading("Montagem e Serviços Industriais", size="9", color="white", text_align="center", margin_bottom="0.2em"),
            rx.text("Especialistas em Caldeiras, Refratários, Tubulações e Estruturas Metálicas de Alta Complexidade.", color="white", max_width="700px", text_align="center", size="5"),
            rx.hstack(
                rx.link(
                    rx.button("Solicite um Orçamento no WhatsApp", color_scheme="green", size="3", radius="full"),
                    href="https://wa.me/5512996014334",
                    is_external=True
                ),
                rx.link(
                    rx.button("Nossos Serviços", variant="outline", color_scheme="cyan", size="3", radius="full"),
                    href="#servicos"
                ),
                spacing="4",
                margin_top="2em"
            ),
            align_items="center",
            justify_content="center",
            height="100vh",
            background_color="rgba(0,0,0,0.7)", # Overlay escuro para a imagem de fundo
            padding="2em"
        ),
        background_image="url('/hero_bg.jpg')",
        background_size="cover",
        background_position="center",
        width="100%"
    )

def about_section():
    return rx.vstack(
        rx.heading("Sobre a Empresa", size="8", color="white", margin_bottom="1em", text_align="center"),
        rx.text(
            "A Qualitec Montagens e Serviços Industriais LTDA atua desde 2017 no segmento de montagem, manutenção e reparos industriais, "
            "oferecendo soluções especializadas para caldeiras, trocadores de calor, condensadores e equipamentos industriais. "
            "Com sede em São José dos Campos, a empresa se destaca pela qualidade técnica, segurança e compromisso com seus clientes, "
            "realizando serviços como substituição de tubulações, reparos estruturais, soldagem TIG, MIG e Eletrodo Revestido, testes hidrostáticos, serviços de refratário industrial. "
            "A Qualitec busca garantir eficiência, confiabilidade e alto padrão em cada projeto executado.",
            color="gray.300", text_align="center", max_width="900px", size="5", line_height="1.6"
        ),
        id="sobre",
        padding_top="6em",
        padding_bottom="2em",
        padding_x=["1em", "2em", "4em"],
        width="100%",
        max_width="1200px",
        margin="0 auto",
        align_items="center"
    )

def service_card(title: str, items: list[str]):
    return rx.card(
        rx.vstack(
            rx.heading(title, size="5", color=primary_color),
            rx.list.unordered(
                *[rx.list.item(item, color="gray.300") for item in items]
            ),
            spacing="3",
            align_items="start"
        ),
        background_color=card_bg,
        border="1px solid rgba(255,255,255,0.05)",
        _hover={"transform": "translateY(-5px)", "transition": "0.3s ease", "border_color": primary_color}
    )

def services_section():
    return rx.vstack(
        rx.heading("Nossos Serviços", size="8", color="white", margin_bottom="1.5em", text_align="center"),
        rx.grid(
            service_card("Inspeção e Soldagem", [
                "Inspeção NR 13 em caldeiras e vasos",
                "Soldagem especializada em tubulações e caldeiras",
                "Reparos de solda em tubos de caldeiras",
                "Profissionais qualificados (EPS, RQPS, RQS, RAS, etc)"
            ]),
            service_card("Tubulações e Caldeiraria", [
                "Instalação de tubulações de aço carbono e aço inoxidável",
                "Serviços de caldeiraria em geral",
                "Troca de seção de chapas em caldeiras"
            ]),
            service_card("Manutenção e Montagem", [
                "Montagens e manutenções em caldeiras novas e usadas",
                "Troca de tubos em caldeiras e trocadores de calor",
                "Troca de tubo para prear"
            ]),
            service_card("Refratários e Isolamento", [
                "Execução de serviços com refratários",
                "Serviços de isolamento térmico",
                "Regulagem de combustão de queimadores para caldeiras e fornalhas"
            ]),
            columns="2",
            spacing="5",
            width="100%"
        ),
        id="servicos",
        padding_top="6em",
        padding_bottom="4em",
        padding_x=["1em", "2em", "4em"],
        width="100%",
        max_width="1200px",
        margin="0 auto"
    )

def portfolio_item(image: str, title: str):
    return rx.vstack(
        rx.image(src=image, border_radius="8px", width="100%", height="250px", object_fit="cover", box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.5)"),
        rx.text(title, color="white", font_weight="bold", text_align="center", margin_top="0.5em"),
        align_items="center"
    )

def portfolio_section():
    return rx.vstack(
        rx.heading("Portfólio & Especialidades", size="8", color="white", margin_bottom="1.5em", text_align="center"),
        rx.grid(
            portfolio_item("/port_1.png", "Manutenção e Reparo Industrial"),
            portfolio_item("/port_2.png", "Revestimento Refratário"),
            portfolio_item("/port_3.png", "Condensador"),
            portfolio_item("/port_4.png", "Preparação do espelho da caldeiraria"),
            portfolio_item("/port_5.png", "Substituição da boca de visita"),
            portfolio_item("/port_6.png", "Trocador de calor em inox"),
            columns="3",
            spacing="5",
            width="100%"
        ),
        id="portfolio",
        padding_y="4em",
        padding_x=["1em", "2em", "4em"],
        width="100%",
        max_width="1200px",
        margin="0 auto"
    )

def clients_section():
    return rx.vstack(
        rx.heading("Principais Clientes", size="8", color="white", margin_bottom="1em", text_align="center"),
        rx.text("Uma equipe treinada e qualificada visando sempre a qualidade da sua mão de obra e material aplicado.", color="gray.300", text_align="center", max_width="800px", margin_bottom="2em"),
        rx.hstack(
            rx.badge("Fernandez Papeis", color_scheme="cyan", size="3", padding="0.5em"),
            rx.badge("Carvalheira Papeis", color_scheme="cyan", size="3", padding="0.5em"),
            rx.badge("Ceratti Alimentos", color_scheme="cyan", size="3", padding="0.5em"),
            rx.badge("Cia Engenharia", color_scheme="cyan", size="3", padding="0.5em"),
            rx.badge("Trane Equipamentos", color_scheme="cyan", size="3", padding="0.5em"),
            rx.badge("Megastem Instrumentação", color_scheme="cyan", size="3", padding="0.5em"),
            wrap="wrap",
            justify="center",
            spacing="3"
        ),
        id="clientes",
        padding_y="4em",
        padding_x=["1em", "2em", "4em"],
        width="100%",
        max_width="1200px",
        margin="0 auto",
        align_items="center"
    )

def contact_section():
    return rx.vstack(
        rx.heading("Entre em Contato", size="8", color="white", margin_bottom="1em"),
        rx.card(
            rx.vstack(
                rx.text("Responsável Técnico & Comercial: Marcio de Castro Santos", color="white", font_weight="bold", size="5", text_align="center"),
                rx.divider(margin_y="1em", border_color="gray.600"),
                rx.hstack(
                    rx.icon(tag="mail", color=primary_color),
                    rx.text("E-mail: qualitec1.servico@gmail.com", color="gray.300"),
                    align_items="center"
                ),
                rx.hstack(
                    rx.icon(tag="phone", color=primary_color),
                    rx.text("Telefones: (12) 9 9601-4334 / (12) 9 8200-0333", color="gray.300"),
                    align_items="center"
                ),
                rx.hstack(
                    rx.icon(tag="map-pin", color=primary_color),
                    rx.text("Av. José Francisco Marcondes, 633 - Jardim Sao Vicente, São José dos Campos - SP", color="gray.300"),
                    align_items="center"
                ),
                rx.text("CNPJ 29.205.571/0001-44", color="gray.400", size="2", margin_top="0.5em"),
                
                rx.divider(margin_y="1em", border_color="gray.600"),
                rx.text("Precisa de um orçamento? Estamos prontos para atender:", color="white", margin_bottom="0.5em"),
                rx.link(
                    rx.button(
                        rx.icon(tag="message-circle"),
                        " Iniciar conversa no WhatsApp",
                        color_scheme="green",
                        size="4",
                        width="100%"
                    ),
                    href="https://wa.me/5512996014334",
                    is_external=True,
                    width="100%"
                ),
                spacing="3",
                align_items="start"
            ),
            background_color=card_bg,
            border="1px solid rgba(255,255,255,0.05)",
            width="100%",
            max_width="750px",
            padding="2em"
        ),
        rx.text("© 2026 Qualitec Montagens Industriais. Todos os direitos reservados.", color="gray.500", size="2", margin_top="4em"),
        id="contato",
        padding_top="4em",
        padding_bottom="2em",
        padding_x=["1em", "2em", "4em"],
        width="100%",
        background_color="rgba(30, 41, 59, 0.3)",
        align_items="center"
    )

def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero_section(),
        about_section(),
        services_section(),
        portfolio_section(),
        clients_section(),
        contact_section(),
        background_color=dark_bg,
        min_height="100vh",
        font_family="Inter, sans-serif",
    )
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="cyan",
    )
)
app.add_page(index, title="Qualitec | Montagem e Serviços Industriais")

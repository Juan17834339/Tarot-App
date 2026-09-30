import streamlit as st
import datetime

# ==========================================
# BASE DE DATOS DE CARTAS RIDER-WAITE (78 Cartas)
# ==========================================

TAROT_DECK = {
    # Arcanos Mayores
    "0. El Loco": {
        "tipo": "Arcano Mayor", "elemento": "Aire",
        "derecho": "Nuevos comienzos, fe ciega, inocencia, espontaneidad, salto de fe.",
        "invertido": "Imprudencia, correr riesgos innecesarios, estancamiento, necedad.",
        "consejo": "Abraza lo desconocido y confía en el proceso sin temor al qué dirán."
    },
    "I. El Mago": {
        "tipo": "Arcano Mayor", "elemento": "Aire",
        "derecho": "Manifestación, recursos, concentración, poder personal, habilidad.",
        "invertido": "Manipulación, talentos no aprovechados, engaño, falta de foco.",
        "consejo": "Tienes todas las herramientas necesarias; es momento de actuar y canalizar tu intención."
    },
    "II. La Sacerdotisa": {
        "tipo": "Arcano Mayor", "elemento": "Agua",
        "derecho": "Intuición, misterio, conocimiento subconsciente, mundo interior, paciencia.",
        "invertido": "Secretos reprimidos, desconexión intuitiva, superficialidad, silencio forzado.",
        "consejo": "Escucha tu voz interior y confía en lo que sientes antes de tomar decisiones precipitadas."
    },
    "III. La Emperatriz": {
        "tipo": "Arcano Mayor", "elemento": "Tierra",
        "derecho": "Abundancia, fertilidad, creatividad, naturaleza, nutrición afectiva.",
        "invertido": "Dependencia, bloqueo creativo, negligencia, sofocación emocional.",
        "consejo": "Nutre tus proyectos con amor y permite que las cosas florezcan a su propio ritmo."
    },
    "IV. El Emperador": {
        "tipo": "Arcano Mayor", "elemento": "Fuego",
        "derecho": "Estructura, autoridad, orden, estabilidad, disciplina, liderazgo.",
        "invertido": "Rigidez, tiranía, falta de disciplina, caos, abuso de poder.",
        "consejo": "Establece límites claros y pon orden en tu vida con firmeza y estrategia."
    },
    "V. El Hierofante": {
        "tipo": "Arcano Mayor", "elemento": "Tierra",
        "derecho": "Tradición, enseñanza, valores morales, guía espiritual, aprendizaje.",
        "invertido": "Rebeldía, dogmatismo, romper reglas obsoletas, no conformidad.",
        "consejo": "Busca orientación en sistemas probados o cuestiona creencias que ya no te sirven."
    },
    "VI. Los Enamorados": {
        "tipo": "Arcano Mayor", "elemento": "Aire",
        "derecho": "Amor, alineación de valores, decisiones de corazón, uniones armoniosas.",
        "invertido": "Desalineación, conflicto de valores, indecisión, desequilibrio en relaciones.",
        "consejo": "Elige desde la honestidad con tus verdaderos valores y comprométete con tu elección."
    },
    "VII. El Carro": {
        "tipo": "Arcano Mayor", "elemento": "Agua",
        "derecho": "Determinación, fuerza de voluntad, victoria, superación de obstáculos.",
        "invertido": "Falta de control, agresión, pérdida de dirección, estancamiento por impulsividad.",
        "consejo": "Toma las riendas con disciplina y mantén el rumbo fijo hacia tu meta."
    },
    "VIII. La Justicia": {
        "tipo": "Arcano Mayor", "elemento": "Aire",
        "derecho": "Equilibrio, verdad, causa y efecto, justicia, responsabilidad, claridad.",
        "invertido": "Injusticia, deshonestidad, falta de responsabilidad, sesgo, impunidad.",
        "consejo": "Actúa con imparcialidad y asume las consecuencias de tus actos con madurez."
    },
    "IX. El Ermitaño": {
        "tipo": "Arcano Mayor", "elemento": "Tierra",
        "derecho": "Introspección, búsqueda de la verdad, soledad constructiva, guía interior.",
        "invertido": "Aislamiento excesivo, aislamiento tóxico, terquedad, desconexión social.",
        "consejo": "Haz una pausa en el ruido externo y busca la respuesta dentro de ti."
    },
    "X. La Rueda de la Fortuna": {
        "tipo": "Arcano Mayor", "elemento": "Fuego",
        "derecho": "Cambios, ciclos de la vida, destino, giros a favor, oportunidades.",
        "invertido": "Mala suerte, resistencia al cambio, contratiempos, aferrarse al pasado.",
        "consejo": "Acepta que el cambio es constante y adáptate con flexibilidad a los giros del destino."
    },
    "XI. La Fuerza": {
        "tipo": "Arcano Mayor", "elemento": "Fuego",
        "derecho": "Valentía, compasión, autocontrol, dominio suave del instinto, resiliencia.",
        "invertido": "Duda personal, debilidad, falta de autocontrol, agresividad o sumisión.",
        "consejo": "Responde con paciencia y amor en lugar de fuerza bruta; la suavidad domina la fiera."
    },
    "XII. El Colgado": {
        "tipo": "Arcano Mayor", "elemento": "Agua",
        "derecho": "Perspectiva diferente, pausa obligada, entrega, sacrificio constructivo.",
        "invertido": "Mártir voluntario, estancamiento inútil, resistencia a ceder, estancamiento.",
        "consejo": "Cambia tu enfoque y acepta la pausa momentánea; no todas las batallas se ganan empujando."
    },
    "XIII. La Muerte": {
        "tipo": "Arcano Mayor", "elemento": "Agua",
        "derecho": "Transformación profunda, finales necesarios, renacimiento, dejar ir.",
        "invertido": "Resistencia al cambio, miedo al cierre, aferrarse a lo caduco.",
        "consejo": "Permite que lo viejo muera para dar espacio a lo nuevo que está por nacer."
    },
    "XIV. La Templanza": {
        "tipo": "Arcano Mayor", "elemento": "Fuego",
        "derecho": "Equilibrio, moderación, paciencia, alquimia interior, propósito claro.",
        "invertido": "Desequilibrio, excesos, impaciencia, falta de armonía.",
        "consejo": "Busca el punto medio y combina con calma los aspectos en conflicto."
    },
    "XV. El Diablo": {
        "tipo": "Arcano Mayor", "elemento": "Tierra",
        "derecho": "Ataduras mentales, obsesión, materialismo, sombras no integradas, tentación.",
        "invertido": "Liberación de adicciones, romper cadenas, tomar conciencia de la ilusión.",
        "consejo": "Reconoce tus propias ataduras mentales; la llave para liberarte siempre ha estado en tus manos."
    },
    "XVI. La Torre": {
        "tipo": "Arcano Mayor", "elemento": "Fuego",
        "derecho": "Revelación repentina, ruptura de ilusiones, cambio drástico, liberación.",
        "invertido": "Evitar el colapso inevitable, miedo a la verdad, desastre pospuesto.",
        "consejo": "Deja que caigan las estructuras falsas; la verdad reconstruirá sobre bases sólidas."
    },
    "XVII. La Estrella": {
        "tipo": "Arcano Mayor", "elemento": "Aire",
        "derecho": "Esperanza, renovación, fe, inspiración, sanación profunda, serenidad.",
        "invertido": "Desesperanza, cinismo, falta de fe, desconexión espiritual.",
        "consejo": "Confía en el futuro y comparte tu luz de manera auténtica y desinteresada."
    },
    "XVIII. La Luna": {
        "tipo": "Arcano Mayor", "elemento": "Agua",
        "derecho": "Ilusiones, subconsciente, miedos, intuición profunda, sombras, confusión.",
        "invertido": "Claridad que emerge, superar ilusiones, revelación de engaños.",
        "consejo": "Navega las sombras de la incertidumbre con cautela sin dejarte llevar por la paranoia."
    },
    "XIX. El Sol": {
        "tipo": "Arcano Mayor", "elemento": "Fuego",
        "derecho": "Éxito, vitalidad, claridad, alegría, abundancia, optimismo.",
        "invertido": "Optimismo excesivo, nubarrones temporales, alegría opacada.",
        "consejo": "Celebra tus logros, exprésate con espontaneidad y disfruta la luz del momento."
    },
    "XX. El Juicio": {
        "tipo": "Arcano Mayor", "elemento": "Fuego",
        "derecho": "Despertar, llamado de vida, evaluación, absolución, toma de conciencia.",
        "invertido": "Autocrítica destructiva, ignorar el llamado, duda, culpa sin resolver.",
        "consejo": "Escucha tu llamado interno y perdónate para avanzar hacia un nuevo nivel de conciencia."
    },
    "XXI. El Mundo": {
        "tipo": "Arcano Mayor", "elemento": "Tierra",
        "derecho": "Compleción, logro total, integración, viajes, cierre de un gran ciclo.",
        "invertido": "Falta de cierre, metas incompletas, atajos frustrados.",
        "consejo": "Reconoce el camino recorrido y celebra la culminación victoriosa de este ciclo."
    },

    # Arcanos Menores - Bastos (Fuego)
    "As de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Chispa creativa, nuevo proyecto, pasión, inspiración.", "invertido": "Retrasos, falta de pasión, bloqueo creativo.", "consejo": "Aprovecha la chispa inicial y actúa sin dudar."},
    "Dos de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Planificación, visión a futuro, decisiones de expansión.", "invertido": "Miedo a lo desconocido, mala planificación, estancamiento.", "consejo": "Amplía tus horizontes y diseña tu plan con visión global."},
    "Tres de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Progreso, exploración, barcos llegando, éxito en expansión.", "invertido": "Retrasos comerciales, falta de previsión, frustración.", "consejo": "Mantén la vista en el horizonte y confía en lo que has puesto en marcha."},
    "Cuatro de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Celebración, hogar, estabilidad, matrimonio, comunidad.", "invertido": "Inestabilidad hogareña, tensiones familiares, cancelación.", "consejo": "Disfruta de los logros alcanzados junto a tus seres queridos."},
    "Cinco de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Competencia, desacuerdos, lucha de egos, tensión sana.", "invertido": "Evitar conflictos necesarios, luchas destructivas, caos.", "consejo": "Defiende tu postura con deportividad sin caer en agresividades inutiles."},
    "Seis de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Victoria, reconocimiento público, éxito, orgullo merecido.", "invertido": "Caída de gracia, ego herido, falta de reconocimiento.", "consejo": "Recibe el reconocimiento con humildad y sigue firme."},
    "Siete de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Defensa de la postura, perseverancia, resistencia victoriosa.", "invertido": "Abrumado, rendición, incapacidad de defenderse.", "consejo": "Mantén la posición firme frente a la presión externa."},
    "Ocho de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Movimiento rápido, noticias veloces, viajes, acción fluida.", "invertido": "Retrasos, malentendidos, acción precipitada sin freno.", "consejo": "Actúa con agilidad pero asegúrate de mantener la dirección correcta."},
    "Nueve de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Resiliencia, última línea de defensa, cautela, perseverancia.", "invertido": "Agotamiento total, paranoia, rendirse antes de la meta.", "consejo": "Resiste un poco más; estás muy cerca de superar el obstáculo."},
    "Diez de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Carga pesada, sobretrabajo, responsabilidad excesiva.", "invertido": "Colapso por estrés, soltar cargas, delegar por fin.", "consejo": "Aprende a delegar; no tienes que llevar todo el peso sobre tus hombros."},
    "Sota de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Mensajero entusiasta, nuevas ideas, curiosidad, aventura.", "invertido": "Imprudencia, malas noticias, falta de compromiso.", "consejo": "Explora nuevas ideas con entusiasmo contagioso."},
    "Caballero de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Acción apasionada, impulso, viaje, intrepidez.", "invertido": "Impulsividad destructiva, impaciencia, arrogancia.", "consejo": "Avanza con valentía pero mide las consecuencias antes de saltar."},
    "Reina de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Carisma, confianza, determinación, calidez, magnetismo.", "invertido": "Jelousia, egoísmo, manipulación, temperamento volcánico.", "consejo": "Irradia tu luz propia y lidera con calidez y seguridad."},
    "Rey de Bastos": {"tipo": "Bastos", "elemento": "Fuego", "derecho": "Liderazgo inspirador, visión, emprendimiento, maestría.", "invertido": "Autoritarismo, expectativas impagables, agresividad.", "consejo": "Inspira a otros con tu ejemplo y visión estratégica."},

    # Arcanos Menores - Copas (Agua)
    "As de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Amor incondicional, nuevo despertar emocional, intuición.", "invertido": "Bloqueo emocional, amor propio deficiente, tristeza.", "consejo": "Abre tu corazón para recibir y dar amor en abundancia."},
    "Dos de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Unión, sociedad armoniosa, conexión profunda, atracción.", "invertido": "Ruptura, malentendidos en la pareja, desconexión.", "consejo": "Fomenta la reciprocidad y el entendimiento mutuo."},
    "Tres de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Amistad, celebración, reunión, alegría compartida.", "invertido": "Excesos sociales, chismes, exclusión de grupo.", "consejo": "Celebra la vida con tu círculo de apoyo y apoyo sincero."},
    "Cuatro de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Apatía, aburrimiento, ignorar oportunidades, introspección.", "invertido": "Despertar del letargo, aceptar nuevas ofertas, renovación.", "consejo": "Abre los ojos a las bendiciones que tienes enfrente y estás ignorando."},
    "Cinco de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Lamento, duelo, foco en lo perdido, melancolía.", "invertido": "Aceptación, superar el pasado, ver lo que aún queda.", "consejo": "Llora lo que fue pero voltea a ver las copas que aún quedan en pie."},
    "Seis de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Nostalgia, recuerdos de infancia, inocencia, reencuentros.", "invertido": "Atrapado en el pasado, aferrarse al ayer, inmadurez.", "consejo": "Honra tus raíces pero vive en el presente activo."},
    "Siete de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Múltiples opciones, fantasías, ilusiones, dispersión.", "invertido": "Claridad mental, elegir una opción concreta, sobriedad.", "consejo": "Diferencia los castillos en el aire de las oportunidades reales."},
    "Ocho de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Dejar atrás lo que no nutre, búsqueda de significado superior.", "invertido": "Miedo al abandono, quedarse en situaciones tóxicas.", "consejo": "Ten el valor de marcharte cuando algo ya no aporta a tu alma."},
    "Nueve de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Satisfacción personal, deseos cumplidos, bienestar, dicha.", "invertido": "Materialismo, engreimiento, insatisfacción interior.", "consejo": "Agradece la plenitud y disfruta de tus logros sin caer en la arrogancia."},
    "Diez de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Felicidad familiar, armonía plena, paz duradera.", "invertido": "Conflictos familiares, valores rotos, desilusión.", "consejo": "Cultiva la paz en tu entorno cercano y valora el amor genuino."},
    "Sota de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Mensajes cariñosos, intuición incipiente, sensibilidad.", "invertido": "Inmadurez emocional, hipersensibilidad, mentiras amorosas.", "consejo": "Abraza tu lado poético y sensible sin miedo al qué dirán."},
    "Caballero de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Propuestas románticas, idealismo, seguir el corazón.", "invertido": "Promesas falsas, manipulación emocional, celos.", "consejo": "Expresa tus sentimientos con elegancia y autenticidad."},
    "Reina de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Empatía, intuición, sanación, compasión, madurez afectiva.", "invertido": "Codependencia, inestabilidad emocional, manipulación.", "consejo": "Escucha tus emociones y ofrece contención desde un centro sano."},
    "Rey de Copas": {"tipo": "Copas", "elemento": "Agua", "derecho": "Control emocional, sabiduría del corazón, diplomacia, calma.", "invertido": "Represión de sentimientos, frialdad calculada, chantaje.", "consejo": "Mantén la calma en medio de la tempestad y decide con empatía y lógica."},

    # Arcanos Menores - Espadas (Aire)
    "As de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Claridad mental, verdad revelada, corte victorioso, avance.", "invertido": "Confusión, mentiras, uso destructivo de la verdad, bloqueo.", "consejo": "Corta con las ilusiones y habla desde la verdad absoluta."},
    "Dos de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Indecisión, dilema, ojos vendados, tregua momentánea.", "invertido": "Sobrecarga de información, elegir a la fuerza, revelación.", "consejo": "Quítate la venda y toma la decisión que has estado posponiendo."},
    "Tres de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Corazón roto, dolor liberador, traición, duelo necesario.", "invertido": "Sanación gradual, perdón, superar la amargura.", "consejo": "Permítete sentir el dolor para poder procesarlo y sanar."},
    "Cuatro de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Reposó mental, meditación, recuperación, pausa estratégica.", "invertido": "Agotamiento extremo, necesidad urgente de descanso, insomnio.", "consejo": "Haz una pausa y dale descanso a tu mente antes de colapsar."},
    "Cinco de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Victoria pirrórica, conflicto amargo, juego sucio, ego.", "invertido": "Deseo de reconciliación, dejar ir el rencor, tregua.", "consejo": "Evalúa si ganar esta discusión realmente vale el precio de la relación."},
    "Seis de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Transición hacia aguas más calmas, viaje, dejar la tormenta.", "invertido": "Resistencia a la transición, equipaje emocional pesado.", "consejo": "Acepta el traslado a una fase más serena, dejando el drama atrás."},
    "Siete de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Estrategia sigilosa, astucia, evitar conflicto directo, secreto.", "invertido": "Confesión, desenmascaramiento, arrepentimiento, engaño descubierto.", "consejo": "Sé inteligente en tu estrategia pero no traiciones tus principios."},
    "Ocho de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Parálisis por análisis, victimismo, ataduras mentales.", "invertido": "Liberación, romper la venda, asumir responsabilidad.", "consejo": "Reconoce que las ataduras son ilusorias y da el paso hacia fuera."},
    "Nueve de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Ansiedad, pesadillas, insomnio, preocupación excesiva.", "invertido": "Superar la desesperación, buscar ayuda, ver la luz.", "consejo": "Recuerda que tus peores pensamientos rara vez se vuelven realidad."},
    "Diez de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Tocar fondo, fin inevitable, traición total, nuevo amanecer.", "invertido": "Resurgir de las cenizas, recuperación lenta, aprendizaje.", "consejo": "Acepta el fin definitivo de esta etapa; el amanecer ya está en camino."},
    "Sota de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Mente curiosa, vigilancia, búsqueda de verdad, mensajes agudos.", "invertido": "Chismes, paranoia, lenguaje hiriente, cinismo.", "consejo": "Observa con atención antes de sacar conclusiones apresuradas."},
    "Caballero de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Acción rápida, ímpetu intelectual, ir directo al grano.", "invertido": "Palabras hirientes, precipitación ciega, agresividad verbal.", "consejo": "Defiende tu verdad con agilidad sin arrollar a los demás."},
    "Reina de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Mente clara, perspicacia, límites sanos, independencia.", "invertido": "Friedad excesiva, amargura, juicio implacable, manipulación.", "consejo": "Decide con lógica e imparcialidad manteniendo tu dignidad."},
    "Rey de Espadas": {"tipo": "Espadas", "elemento": "Aire", "derecho": "Autoridad intelectual, ética, claridad analítica, justicia.", "invertido": "Tiranía mental, uso cruento del intelecto, corrupción.", "consejo": "Aplica la lógica y la ley con equidad incorruptible."},

    # Arcanos Menores - Oros / Pentáculos (Tierra)
    "As de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Nueva oportunidad material, manifestación, salud, regalo divino.", "invertido": "Oportunidad perdida, mala inversión, inestabilidad física.", "consejo": "Aprovecha esta semilla tangible para construir estabilidad a largo plazo."},
    "Dos de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Manejo de prioridades, flexibilidad, malabares financieros.", "invertido": "Desequilibrio, sobrecarga financiera, falta de organización.", "consejo": "Mantén la adaptabilidad sin descuidar lo verdaderamente importante."},
    "Tres de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Trabajo en equipo, colaboración, maestría, reconocimiento profesional.", "invertido": "Falta de cooperación, trabajo mediocre, desorganización.", "consejo": "Colabora con expertos y enfócate en la calidad del detalle."},
    "Cuatro de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Ahorro, conservación, seguridad, tacañería o apego excesivo.", "invertido": "Derroche, soltar el control financiero, generosidad forzada.", "consejo": "Protege tus recursos sin dejar que el miedo al despojo te paralice."},
    "Cinco de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Dificultad material, sensación de aislamiento, rechazo, frío.", "invertido": "Superación de la crisis, encontrar ayuda, recuperar la salud.", "consejo": "Recuerda que la ayuda está disponible si te atreves a tocar la puerta."},
    "Seis de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Generosidad, dar y recibir, equilibrio financiero, caridad.", "invertido": "Deudas, condiciones abusivas, generosidad interesada.", "consejo": "Comparte tus bendiciones y acepta el apoyo cuando lo necesites."},
    "Siete de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Paciencia, evaluación de la cosecha, inversión a largo plazo.", "invertido": "Impaciencia, frutos estériles, frustración por lentitud.", "consejo": "Ten paciencia; las semillas bien sembradas requieren tiempo para dar fruto."},
    "Ocho de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Dedicación, artesanía, desarrollo de habilidades, constancia.", "invertido": "Falta de esfuerzo, perfectionismo paralizante, trabajo rutinario.", "consejo": "Pule tus habilidades con disciplina cotidiana y amor por el detalle."},
    "Nueve de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Independencia financiera, autosuficiencia, disfrute del lujo sano.", "invertido": "Vivir por encima de los medios, soledad de oro, dependencia.", "consejo": "Disfruta el fruto de tu trabajo autónomo con orgullo y gracia."},
    "Diez de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Riqueza heredada, estabilidad intergeneracional, legado duradero.", "invertido": "Pérdida de herencia, tensiones familiares por dinero, ruina.", "consejo": "Construye bases sólidas que trasciendan y brinden paz a los tuyos."},
    "Sota de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Estudiante dedicado, nuevas ofertas de trabajo o estudio, metas.", "invertido": "Falta de progreso, procrastinación, metas poco realistas.", "consejo": "Aplica la disciplina en el estudio y toma tus responsabilidades en serio."},
    "Caballero de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Trabajo metódico, lealtad, perseverancia, progreso constante.", "invertido": "Terquedad, aburrimiento rutinario, pereza, estancamiento.", "consejo": "Avanza paso a paso con constancia inquebrantable."},
    "Reina de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Pragmatismo, abundancia del hogar, hospitalidad, nutrición.", "invertido": "Materialismo excesivo, desatención del hogar, inseguridad.", "consejo": "Crea un entorno acogedor y gestiona tus recursos con sabiduría práctica."},
    "Rey de Oros": {"tipo": "Oros", "elemento": "Tierra", "derecho": "Éxito financiero, maestría empresarial, seguridad, proveedor.", "invertido": "Avaricia, obsesión por el dinero, corrupción, rigidez.", "consejo": "Gestiona tu imperio material con ética, visión y generosidad."}
}

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA STREAMLIT
# ==========================================

st.set_page_config(
    page_title="Tarot Rider-Waite | Aplicación de Lectura",
    page_icon="🔮",
    layout="wide"
)

# Estilo visual personalizado
st.markdown("""
<style>
    .stApp {
        background-color: #0f0e17;
        color: #fffffe;
    }
    .main-header {
        text-align: center;
        color: #ffd700;
        font-family: 'Georgia', serif;
        padding-bottom: 20px;
    }
    .card-box {
        background-color: #16161a;
        border: 1px solid #7f5af0;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .card-title {
        color: #ffd700;
        font-weight: bold;
        font-size: 1.1em;
    }
    .interpretation-container {
        background-color: #1f1b24;
        border-left: 5px solid #ffd700;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🔮 Oráculo del Tarot Rider-Waite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a7a9be;'>Aplicación de Lectura e Interpretación Terapéutica y Sistemática</p>", unsafe_allow_html=True)

# ==========================================
# SECCIÓN 1: DATOS DEL CONSULTANTE Y PREGUNTA
# ==========================================

st.sidebar.header("📋 Configuración de la Sesión")
nombre_consultante = st.sidebar.text_input("Nombre del Consultante", value="Elena")
pregunta = st.sidebar.text_area("Formulación de la Pregunta / Inquietud", value="¿Qué necesito comprender para desbloquear mi creatividad y lanzar mi nuevo proyecto?")

tipo_tirada = st.sidebar.selectbox(
    "Selecciona la Tirada",
    ["1 Carta (Mensaje Diario)", "3 Cartas (Situación - Desafío - Consejo)", "Cruz Celta (10 Cartas)"]
)

st.sidebar.markdown("---")
modo_ingreso = st.sidebar.radio("Modo de selección de cartas", ["Ingreso Manual (Lectura Física)", "Extracción Aleatoria (Mazo Digital)"])

# Definiendo las posiciones según la tirada
if tipo_tirada == "1 Carta (Mensaje Diario)":
    posiciones = ["Mensaje del Día / Enfoque Principal"]
elif tipo_tirada == "3 Cartas (Situación - Desafío - Consejo)":
    posiciones = ["1. Situación Actual", "2. El Desafío / Bloqueo", "3. El Consejo / Solución"]
else:
    posiciones = [
        "1. El Núcleo / Estado Presente",
        "2. El Desafío Inmediato",
        "3. La Base Subconsciente",
        "4. El Pasado Reciente",
        "5. La Coronación (Mente Consciente)",
        "6. El Futuro Cercano",
        "7. La Actitud del Consultante",
        "8. El Entorno e Influencias Externas",
        "9. Esperanzas y Temores",
        "10. El Resultado Probable"
    ]

# Lista de nombres de cartas
cartas_list = list(TAROT_DECK.keys())

st.subheader("🃏 Extracción e Ingreso de Cartas")

cartas_seleccionadas = []

import random

col1, col2 = st.columns([2, 1])

with col1:
    for idx, pos_nombre in enumerate(posiciones):
        st.markdown(f"**Posición:** `{pos_nombre}`")
        c1, c2 = st.columns([3, 2])
        
        if modo_ingreso == "Ingreso Manual (Lectura Física)":
            default_card_idx = (idx * 5) % len(cartas_list)
            carta_elegida = c1.selectbox(f"Carta para {pos_nombre}", cartas_list, index=default_card_idx, key=f"select_{idx}")
            orientacion = c2.radio(f"Orientación", ["Al Derecho", "Invertida"], key=f"orient_{idx}", horizontal=True)
        else:
            # Extracción Aleatoria
            carta_elegida = random.choice(cartas_list)
            orientacion = random.choice(["Al Derecho", "Invertida"])
            c1.info(f"**Carta:** {carta_elegida}")
            c2.write(f"**Estado:** {orientacion}")
            
        cartas_seleccionadas.append({
            "posicion": pos_nombre,
            "carta": carta_elegida,
            "orientacion": orientacion,
            "datos": TAROT_DECK[carta_elegida]
        })

with col2:
    st.markdown("### 📜 Carta del Fondo del Mazo")
    st.caption("Revela el motor subconsciente o la energía oculta de la consulta.")
    if modo_ingreso == "Ingreso Manual (Lectura Física)":
        fondo_carta = st.selectbox("Carta en la base del mazo", cartas_list, index=0, key="fondo_select")
        fondo_orient = st.radio("Orientación base", ["Al Derecho", "Invertida"], key="fondo_orient", horizontal=True)
    else:
        fondo_carta = random.choice(cartas_list)
        fondo_orient = "Al Derecho"
        st.info(f"**Carta:** {fondo_carta}")
    
    datos_fondo = TAROT_DECK[fondo_carta]

# ==========================================
# SECCIÓN 2: BOTÓN DE INTERPRETACIÓN Y MOTOR SINTÉTICO
# ==========================================

st.markdown("---")

if st.button("✨ Realizar Interpretación de la Lectura", type="primary", use_container_width=True):
    st.markdown("<h2 class='main-header'>✨ Informe de Interpretación Integral</h2>", unsafe_allow_html=True)
    
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Encabezado del informe
    st.markdown(f"""
    <div class='interpretation-container'>
        <h3>👤 Consultante: <span style='color: #ffd700;'>{nombre_consultante}</span></h3>
        <p><strong>📅 Fecha de la Sesión:</strong> {fecha_actual}</p>
        <p><strong>❓ Pregunta / Inquietud:</strong> <em>«{pregunta}»</em></p>
        <p><strong>🔮 Tirada Seleccionada:</strong> {tipo_tirada}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 Análisis Detallado Carta por Carta")
    
    elementos_conteo = {"Fuego": 0, "Agua": 0, "Aire": 0, "Tierra": 0}
    arcanos_mayores_conteo = 0
    
    for c in cartas_seleccionadas:
        info = c["datos"]
        elem = info["elemento"]
        elementos_conteo[elem] = elementos_conteo.get(elem, 0) + 1
        if info["tipo"] == "Arcano Mayor":
            arcanos_mayores_conteo += 1
            
        significado = info["derecho"] if c["orientacion"] == "Al Derecho" else info["invertido"]
        
        st.markdown(f"""
        <div class='card-box'>
            <span class='card-title'>📌 {c['posicion']}: {c['carta']} ({c['orientacion']})</span><br/>
            <small style='color: #a7a9be;'>Tipo: {info['tipo']} | Elemento: {info['elemento']}</small>
            <p style='margin-top: 8px;'><strong>Significado en esta posición:</strong> {significado}</p>
            <p style='color: #2cb67d; margin-bottom: 0;'>💡 <strong>Consejo Clave:</strong> {info['consejo']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    # Fondo del mazo
    st.markdown(f"""
    <div class='card-box' style='border-color: #ffd700;'>
        <span class='card-title'>🌌 Fondo del Mazo (Subconsciente): {fondo_carta} ({fondo_orient})</span><br/>
        <p><strong>Influencia Oculta:</strong> {datos_fondo['derecho'] if fondo_orient == 'Al Derecho' else datos_fondo['invertido']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # SÍNTESIS HOLÍSTICA
    st.markdown("### 🧩 Síntesis y Conclusión Terapéutica")
    
    # Elemento dominante
    elem_dominante = max(elementos_conteo, key=elementos_conteo.get)
    
    sintesis_text = f"Hola **{nombre_consultante}**, respondiendo directamente a tu inquietud sobre *«{pregunta}»*:\n\n"
    
    if arcanos_mayores_conteo > (len(posiciones) / 2):
        sintesis_text += f"• **Nivel de Transformación:** Hay una alta presencia de Arcanos Mayores ({arcanos_mayores_conteo} de {len(posiciones)} cartas). Esto señala que estás atravesando un proceso de aprendizaje profundo y lecciones de vida importantes, donde el destino y los arquetipos principales están en juego.\n"
    else:
        sintesis_text += f"• **Nivel Práctico y Cotidiano:** La lectura muestra mayor presencia de Arcanos Menores, lo que indica que la resolución depende de tus acciones, decisiones diarias y ajuste de hábitos inmediatos.\n"
        
    sintesis_text += f"• **Dinámica Elemental Predominante ({elem_dominante}):** La energía de **{elem_dominante}** es la más fuerte en esta tirada. "
    if elem_dominante == "Fuego":
        sintesis_text += "Esto indica la necesidad de enfocar la pasión, la motivación, la iniciativa y la fuerza de voluntad."
    elif elem_dominante == "Agua":
        sintesis_text += "Esto resalta que las emociones, la intuición, los lazos afectivos y la sanación interna son el eje central."
    elif elem_dominante == "Aire":
        sintesis_text += "Esto revela que el pensamiento, la claridad mental, la comunicación y superar la parálisis por análisis son determinantes."
    else:
        sintesis_text += "Esto demuestra que la estabilidad material, la salud, la constancia y los recursos concretos son la clave."
        
    st.info(sintesis_text)
    
    # Descargar informe
    reporte_txt = f"LECTURA DE TAROT RIDER-WAITE\nConsultante: {nombre_consultante}\nFecha: {fecha_actual}\nPregunta: {pregunta}\nTirada: {tipo_tirada}\n\nCARTAS:\n"
    for c in cartas_seleccionadas:
        reporte_txt += f"- {c['posicion']}: {c['carta']} ({c['orientacion']})\n"
    reporte_txt += f"\nFondo del Mazo: {fondo_carta}\n\nSÍNTESIS:\n{sintesis_text}"
    
    st.download_button("📥 Descargar Informe Completo (TXT)", reporte_txt, file_name=f"lectura_tarot_{nombre_consultante.lower()}.txt")

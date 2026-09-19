ESTIMATION_EXAMPLES = [
    {
        "meeting_summary": "El cliente necesita migrar una instalación *on-premise* de SAP S/4HANA 2022 alojada en Google Cloud Platform a SAP RISE versión 2025",
        "estimation": """
        ## Estimación: Migracion a Rise
        
        ### Desglose de tareas:
        1. Adaptación de programas ABAP: 120 horas
        2. Migración de código: 60 horas
        3. Pruebas post-migración: 60 horas
        4. Exportación y carga en el nuevo entorno: 60 horas
        5. Testing y QA: 100 horas
        
        **Total estimado: 400 horas**
        **Equipo recomendado: 1 Consultor de SAP BASIS 2 desarrolladores ABAP + 1 tester (part-time)**
        **Duración estimada: 6-8 semanas**
        """
    },
    
    # Proyecto 2: E-commerce Salesforce
{
    "meeting_summary": "El cliente requiere implementar una solución de e-commerce utilizando Salesforce Commerce Cloud con integración a su backend legacy y personalización de la experiencia de compra",
    "estimation": """

    ## Estimación: Implementación E-commerce Salesforce
    
    ### Desglose de tareas:
    1. Configuración de Salesforce Commerce Cloud (SFCC): 80 horas
    2. Integración de catálogo de productos y sincronización: 100 horas
    3. Desarrollo de flujo de checkout y pasarelas de pago: 90 horas
    4. Personalización de templates y front-end (SFRA/PWA): 120 horas
    5. Integración con sistemas legacy (ERP, CRM): 70 horas
    6. Testing (funcional, integración, UAT): 60 horas
    
    **Total estimado: 520 horas**
    **Equipo recomendado: 1 Arquitecto Salesforce Commerce + 2 Desarrolladores SFCC/JavaScript + 1 Especialista en Integraciones + 1 QA**
    **Duración estimada: 8-10 semanas**
    """
},

# Proyecto 3: Gestión de Tiendas - Java y Angular
{
    "meeting_summary": "Desarrollo de una aplicación web full-stack para la gestión centralizada de múltiples sucursales/tiendas con módulos de inventario, ventas y reportería",
    "estimation": """,
    ## Estimación: App Gestión de Tiendas (Java + Angular)
    
    ### Desglose de tareas:
    1. Arquitectura y diseño de base de datos: 60 horas
    2. Desarrollo backend Spring Boot/Java (APIs REST): 180 horas
    3. Autenticación, autorización y seguridad: 70 horas
    4. Desarrollo frontend Angular (módulos y componentes): 200 horas
    5. Integración de reportería y dashboards: 80 horas
    6. Optimización, testing unitario e integración: 90 horas
    
    **Total estimado: 680 horas**
    **Equipo recomendado: 1 Tech Lead/Arquitecto Java + 2 Desarrolladores Backend + 2 Desarrolladores Frontend Angular + 1 Especialista QA + 1 DBA (part-time)**
    **Duración estimada: 10-12 semanas**
    """
}
]


def format_examples_for_prompt(examples: list[dict]) -> str:
    """Render the reference examples as a numbered text block for the LLM prompt."""
    blocks = []
    for index, example in enumerate(examples, start=1):
        blocks.append(
            f"### Ejemplo {index}\n"
            f"Resumen de reunión: {example['meeting_summary']}\n"
            f"Estimación:\n{example['estimation']}"
        )
    return "\n\n".join(blocks)
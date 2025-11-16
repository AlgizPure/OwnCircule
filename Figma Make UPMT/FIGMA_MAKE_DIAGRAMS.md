# FIGMA MAKE + UPMT PROCESS FLOW

## Визуализация полного процесса

```mermaid
flowchart TB
    Start([UPMT Bootstrap Start]) --> P1[PHASE 1: Analysis]
    P1 --> P2[PHASE 2: Interview]
    P2 --> P3[PHASE 3: Tech Verification]
    P3 --> P4[PHASE 4: Synthesis]
    
    P4 --> P5[PHASE 5: Documentation]
    
    P5 --> Q{Хочешь Figma Make<br/>прототип?}
    
    Q -->|YES| P54[PHASE 5.4: Generate Prompt]
    Q -->|NO| P55Check{Design Raw<br/>Data exists?}
    
    P54 --> GenPrompt[Генерация промпта<br/>3000+ слов]
    GenPrompt --> ValidPrompt{Validation<br/>passed?}
    ValidPrompt -->|NO| FixPrompt[Fix Issues]
    FixPrompt --> GenPrompt
    ValidPrompt -->|YES| SavePrompt[Save FIGMA_MAKE_PROMPT.md]
    
    SavePrompt --> UserAction[USER ACTION:<br/>Работа с Figma Make<br/>2-3 часа]
    
    UserAction --> FigmaWork[1. Copy prompt<br/>2. Generate in Figma Make<br/>3. Iterate<br/>4. Export results]
    
    FigmaWork --> SaveExports[Save to<br/>00_DESIGN_RAW_DATA/<br/>figma-make/exports/]
    
    SaveExports --> P55[PHASE 5.5: Design System]
    P55Check -->|YES| P55
    P55Check -->|NO| P6[PHASE 6: Setup]
    
    P55 --> AnalyzeFigma{Figma exports<br/>found?}
    AnalyzeFigma -->|YES| UseFigma[Use Figma data<br/>as primary source]
    AnalyzeFigma -->|NO| UseRaw[Use Raw Data<br/>if available]
    
    UseFigma --> CreateDesign[Create Design Docs]
    UseRaw --> CreateDesign
    
    CreateDesign --> P6
    
    P6 --> P7[PHASE 7: Validation]
    P7 --> P8[PHASE 8: Final Report]
    P8 --> Done([Bootstrap Complete!])
    
    Done --> Result[✅ MVP Prototype<br/>✅ Design Docs<br/>✅ Working Code]
    
    style P54 fill:#e0f2fe,stroke:#0ea5e9,stroke-width:3px
    style UserAction fill:#fef3c7,stroke:#f59e0b,stroke-width:3px
    style FigmaWork fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style SaveExports fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style Result fill:#dcfce7,stroke:#10b981,stroke-width:3px
    style Q fill:#fce7f3,stroke:#ec4899,stroke-width:2px
```

## Data Flow Diagram

```mermaid
flowchart LR
    subgraph "INPUT SOURCES"
        A[extracted_features.md<br/>Функции по модулям]
        B[modules_list.md<br/>Список модулей]
        C[metadata.yaml<br/>Метаданные проекта]
        D[PROJECT_SYNTHESIS.md<br/>Unified view]
        E[final-tech-stack.md<br/>Tech stack]
    end
    
    subgraph "PHASE 5.4: PROCESSING"
        F[Template<br/>FIGMA_MAKE_PROMPT_TEMPLATE.md]
        G[Smart Variable<br/>Replacement]
        H[Intelligent<br/>Inference]
        I[Validation<br/>Quality Checks]
    end
    
    subgraph "OUTPUT"
        J[FIGMA_MAKE_PROMPT.md<br/>3000+ words]
        K[README.md<br/>Instructions]
    end
    
    subgraph "USER WORK"
        L[Figma Make<br/>Generation]
        M[Iterations<br/>& Refinement]
    end
    
    subgraph "EXPORT RESULTS"
        N[Screenshots<br/>PNG files]
        O[Design Tokens<br/>JSON]
        P[Figma Link<br/>URL]
    end
    
    subgraph "PHASE 5.5: FINAL DOCS"
        Q[Design System<br/>Documentation]
        R[Component<br/>Library]
    end
    
    A & B & C & D & E --> F
    F --> G
    G --> H
    H --> I
    I --> J
    J --> K
    
    K --> L
    L --> M
    M --> N & O & P
    
    N & O & P --> Q
    Q --> R
    
    style F fill:#ddd6fe,stroke:#8b5cf6
    style G fill:#ddd6fe,stroke:#8b5cf6
    style H fill:#ddd6fe,stroke:#8b5cf6
    style I fill:#ddd6fe,stroke:#8b5cf6
    style J fill:#bbf7d0,stroke:#10b981,stroke-width:3px
    style L fill:#fef3c7,stroke:#f59e0b
    style M fill:#fef3c7,stroke:#f59e0b
    style Q fill:#dcfce7,stroke:#10b981,stroke-width:2px
    style R fill:#dcfce7,stroke:#10b981,stroke-width:2px
```

## Architecture Overview

```mermaid
graph TB
    subgraph "UPMT CORE"
        UPMT[UPMT Repository]
        RawData[00_RAW_DATA_TEMPLATE]
        DesignData[00_DESIGN_RAW_DATA]
    end
    
    subgraph "NEW INTEGRATION"
        Template[Prompt Template]
        Phase54[PHASE 5.4]
        FigmaFolder[figma-make/ folder]
    end
    
    subgraph "FIGMA ECOSYSTEM"
        FigmaMake[Figma Make AI]
        FigmaFile[Figma File]
        Exports[Exports]
    end
    
    subgraph "OUTPUTS"
        Docs[Design Docs]
        Code[Working Code]
        Proto[Interactive Prototype]
    end
    
    UPMT --> RawData
    RawData --> Phase54
    Template --> Phase54
    Phase54 --> FigmaFolder
    
    FigmaFolder --> FigmaMake
    FigmaMake --> FigmaFile
    FigmaFile --> Exports
    
    Exports --> DesignData
    DesignData --> Docs
    FigmaFile --> Code
    FigmaFile --> Proto
    
    style Phase54 fill:#e0f2fe,stroke:#0ea5e9,stroke-width:3px
    style FigmaMake fill:#fef3c7,stroke:#f59e0b,stroke-width:3px
    style Docs fill:#dcfce7,stroke:#10b981
    style Code fill:#dcfce7,stroke:#10b981
    style Proto fill:#dcfce7,stroke:#10b981
```

## Timeline Comparison

```mermaid
gantt
    title Design Creation Time: Traditional vs UPMT+Figma
    dateFormat X
    axisFormat %H:%M
    
    section Traditional
    Initial Mockups       :done, t1, 0, 24h
    Iterations           :done, t2, 24h, 48h
    High-fidelity Design :done, t3, 48h, 96h
    Component Library    :done, t4, 96h, 144h
    Documentation        :done, t5, 144h, 168h
    Total (1 week)       :milestone, 168h, 0h
    
    section UPMT + Figma Make
    Bootstrap (PHASE 1-5) :active, u1, 0, 2h
    Generate Prompt (5.4) :active, u2, 2h, 2.5h
    Figma Make Work      :crit, u3, 2.5h, 5h
    Design Docs (5.5)    :active, u4, 5h, 6h
    Total (6 hours)      :milestone, 6h, 0h
```

## Component Inference Logic

```mermaid
flowchart TD
    Start([User Function]) --> Analyze[Analyze Description]
    
    Analyze --> Create{Contains<br/>'create'<br/>'add'?}
    Analyze --> List{Contains<br/>'list'<br/>'view all'?}
    Analyze --> Edit{Contains<br/>'edit'<br/>'update'?}
    Analyze --> Delete{Contains<br/>'delete'<br/>'remove'?}
    
    Create -->|YES| CompCreate[+ Form<br/>+ Input Fields<br/>+ Primary Button<br/>+ Validation]
    List -->|YES| CompList[+ Table/Grid<br/>+ Search<br/>+ Filter<br/>+ Pagination]
    Edit -->|YES| CompEdit[+ Pre-filled Form<br/>+ Save Button<br/>+ Cancel Button]
    Delete -->|YES| CompDelete[+ Confirm Modal<br/>+ Destructive Button<br/>+ Cancel Option]
    
    CompCreate --> Combine[Combine All<br/>Components]
    CompList --> Combine
    CompEdit --> Combine
    CompDelete --> Combine
    
    Combine --> Screen[Generate Screen<br/>Description]
    Screen --> Output([Component List<br/>for Module])
    
    style Start fill:#e0f2fe
    style Output fill:#dcfce7,stroke:#10b981,stroke-width:2px
    style Combine fill:#fef3c7
```

## Quality Validation Flow

```mermaid
flowchart TB
    Prompt[Generated Prompt] --> Check1{Specificity<br/>Check}
    
    Check1 -->|PASS| Check2{Completeness<br/>Check}
    Check1 -->|FAIL| Fix1[Add:<br/>- HEX codes<br/>- px values<br/>- Font names]
    
    Check2 -->|PASS| Check3{Structure<br/>Check}
    Check2 -->|FAIL| Fix2[Add:<br/>- Missing modules<br/>- Missing functions<br/>- Missing flows]
    
    Check3 -->|PASS| Check4{Consistency<br/>Check}
    Check3 -->|FAIL| Fix3[Fix:<br/>- Word count<br/>- Sections<br/>- Templates]
    
    Check4 -->|PASS| Score{Quality<br/>Score<br/>>= 85%?}
    Check4 -->|FAIL| Fix4[Fix:<br/>- Naming<br/>- Spacing<br/>- Components]
    
    Fix1 --> Check1
    Fix2 --> Check2
    Fix3 --> Check3
    Fix4 --> Check4
    
    Score -->|YES| Ready[✅ Ready for<br/>Figma Make]
    Score -->|NO| Improve[Manual<br/>Review Needed]
    
    Improve --> Check1
    
    style Ready fill:#dcfce7,stroke:#10b981,stroke-width:3px
    style Improve fill:#fef3c7,stroke:#f59e0b
```

---

## Используй эти диаграммы для:

1. **Понимания процесса** - как всё работает end-to-end
2. **Презентаций** - показать стейкхолдерам workflow
3. **Документации** - включить в README или guides
4. **Обучения** - объяснить новым пользователям

Все диаграммы в Mermaid формате - можно рендерить в:
- GitHub README
- GitLab
- Notion
- VS Code (с плагином)
- Confluence
- Markdown viewers

---

**Создано для UPMT + Figma Make Integration**  
**Date:** 2025-11-16

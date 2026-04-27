# Daily Reflection Tree - Visual Logic Map

This diagram represents the deterministic flow of the Daily Reflection tool. It tracks three psychological axes: Locus (Victim vs. Victor), Orientation (Entitlement vs. Contribution), and Radius (Self-Centric vs. Altrocentric).

```mermaid
graph TD
    %% Start Node
    start((Start)) --> q_energy[q_energy_check]

    %% Axis 1: Locus
    q_energy -->|Drained/Neutral| q_friction[q_locus_friction]
    q_energy -->|Satisfied| q_impact[q_locus_impact]
    
    q_friction -->|World/Others| d_victim{d_locus_victim}
    q_friction -->|Puzzle| d_victor{d_locus_victor}
    
    q_impact -->|Luck| d_victim
    q_impact -->|Effort/Team| d_victor
    
    d_victim --> r_victim[r_locus_victim]
    d_victor --> r_victor[r_locus_victor]
    
    r_victim --> bridge1[bridge_locus_orientation]
    r_victor --> bridge1
    
    %% Axis 2: Orientation
    bridge1 --> q_focus[q_orientation_focus]
    
    q_focus -->|Noticed/Checklist| q_entitle[q_entitlement_check]
    q_focus -->|Helped Team| q_contrib[q_contribution_check]
    
    q_entitle -->|Frustrated/Harder| d_entitle{d_orientation_entitled}
    q_entitle -->|Adjusted| d_contrib{d_orientation_contributor}
    
    q_contrib -->|Rewarding/Natural| d_contrib
    q_contrib -->|Fair Trade| d_entitle
    
    d_entitle --> r_entitle[r_orientation_entitled]
    d_contrib --> r_contrib[r_orientation_contributor]
    
    r_entitle --> bridge2[bridge_orientation_radius]
    r_contrib --> bridge2
    
    %% Axis 3: Radius
    bridge2 --> q_scope[q_radius_scope]
    
    q_scope -->|Backlog| q_narrow[q_radius_narrow]
    q_scope -->|User/Mission| q_wide[q_radius_wide]
    
    q_narrow -->|What's next| d_self{d_radius_self}
    q_narrow -->|Others/Team| d_altro{d_radius_altro}
    
    q_wide -->|Considered Needs/Picture| d_altro
    q_wide -->|Deadlines| d_self
    
    d_self --> r_self[r_radius_self]
    d_altro --> r_altro[r_radius_altro]
    
    r_self --> summary[summary_node]
    r_altro --> summary
    
    %% End
    summary --> end_node((End))

    %% Styling
    style start fill:#f9f,stroke:#333,stroke-width:4px
    style end_node fill:#f9f,stroke:#333,stroke-width:4px
    style d_victim fill:#ffcccb
    style d_victor fill:#ccffcc
    style d_entitle fill:#ffcccb
    style d_contrib fill:#ccffcc
    style d_self fill:#ffcccb
    style d_altro fill:#ccffcc
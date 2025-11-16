        phase_3:
          - Gradual rollout to users
          - 10% → 50% → 100%
          - Monitor email deliverability
        
        rollback_plan:
          - Feature flag to disable
          - Queue system allows pause
          - No data loss if disabled
  
  Step 5.2: Performance Considerations
    warn_about:
      - Queue system load
      - Email sending limits
      - Database write load
      - WebSocket connections (if used)
    
    recommend:
      - Load testing before release
      - Rate limiting on notifications
      - Batching for email
      - Caching for preferences
  
  Step 5.3: Cost Considerations
    estimate_costs:
      email_service:
        - SendGrid: $19.95/mo (40k emails)
        - AWS SES: $0.10/1000 emails
      
      push_notifications:
        - Firebase: Free (unlimited)
      
      queue_system:
        - Bull (Redis): Self-hosted
        - AWS SQS: $0.40/million requests
      
      total_monthly: "$20-50 depending on volume"
    
    inform_user: true

**END OF SCENARIO F-02**

---

## Scenario F-03: Scope Reduction (Cutting Features)

**Описание:** Нужно убрать фичу из текущей фазы из-за timeline/budget

**Пример:** "Не успеваем, уберем Social Login из MVP"

### Detailed Workflow:
PHASE 1: IDENTIFY & ANALYZE (5 min)
  
  Step 1.1: Find Feature in Documentation
    search_files:
      - PRD.md: Find feature section
      - ROADMAP.md: Confirm current phase
      - [module]_requirements.md: Check if work started
    
    extract_info:
      feature_name: "Social Login (Google/Facebook)"
      current_phase: "MVP"
      priority: "Should Have"
      status: "Not Started" | "In Progress" | "Complete"
      effort_estimate: "5-7 days"
      module: "Auth"
  
  Step 1.2: Check Dependencies
    analyze_dependencies:
      find_features_that_depend_on_this:
        query: "What features require Social Login?"
        
        found:
          - None (independent feature)
      
      find_features_this_depends_on:
        query: "What does Social Login need?"
        
        found:
          - Auth module base (FR-AUTH-001 through 004)
          - Already implemented
  
  Step 1.3: Impact Assessment
    determine_impact:
      on_product:
        - Users cannot login with Google/Facebook
        - Must use email/password only
        - Slightly reduced convenience
        - Core functionality NOT affected
      
      on_timeline:
        - Frees up: 5-7 days
        - MVP can finish on time
      
      on_code:
        if_not_started:
          - No code to remove
          - Clean cut
        if_in_progress:
          - May have partial implementation
          - Need to remove/comment code
          - Potential for technical debt
      
      on_users:
        - Minor inconvenience
        - Can add later (Phase 1)
        - Acceptable trade-off

PHASE 2: GET CONFIRMATION (2 min)
  
  Step 2.1: Present Analysis
    show_user: |
      📊 FEATURE REMOVAL ANALYSIS: Social Login
      
      📍 CURRENT STATUS:
      - Feature: Social Login (Google, Facebook)
      - Phase: MVP
      - Priority: Should Have
      - Status: Not Started
      - Effort: 5-7 days
      
      🔍 DEPENDENCIES:
      - No features depend on this ✓
      - Independent feature ✓
      - Safe to remove ✓
      
      ✅ BENEFITS OF REMOVAL:
      - Frees up: 5-7 days
      - MVP timeline: Back on track
      - Team: Reduced pressure
      - Focus: Core features only
      
      ⚠️ CONSEQUENCES:
      - Users must use email/password login
      - Slightly less convenient onboarding
      - Can add back in Phase 1
      
      💡 RECOMMENDATION:
      SAFE TO REMOVE - minimal impact on core value proposition
      
      📋 ALTERNATIVE:
      - Keep in MVP but move different "Should Have" feature
      
      Confirm removal of Social Login from MVP? (yes/no/move different feature)
  
  wait_for_confirmation: true
  
  if_no:
    ask: "Which feature should we remove instead?"
    restart_scenario_with_different_feature: true
  
  if_yes:
    proceed: true

PHASE 3: UPDATE DOCUMENTATION (10 min)
  
  Step 3.1: Update PRD
    file: /PROJECT_CORE/01_PRD.md
    
    find_feature_section: "4.7 Social Login"
    
    action: MOVE_TO_PHASE_1 (not delete, for future)
    
    changes:
      - Update **Phase:** "MVP" → "Phase 1"
      - Add note:
          
**Note:** Originally planned for MVP, moved to Phase 1 
          on [date] due to timeline constraints. Core functionality 
          (email/password login) remains in MVP.

      - Keep Priority: "Should Have" (unchanged)
      - Keep all User Stories (unchanged)
    
    version: MINOR bump (1.6 → 1.7)
    
    changelog: |
      ### v1.7 - [date]
      - Changed: Section 4.7 Social Login moved from MVP to Phase 1
      - Reason: Timeline optimization
      - Impact: MVP scope reduced, timeline preserved
  
  Step 3.2: Update ROADMAP
    file: /PROJECT_CORE/02_ROADMAP.md
    
    find_mvp_section:
      locate: "### PHASE 0: MVP"
      subsection: "**Key Features:**"
    
    remove_line: "- [ ] Social Login (Google, Facebook) - Status: Not Started"
    
    find_phase_1_section:
      locate: "### PHASE 1: [Name]"
      subsection: "**Key Features:**"
    
    add_line: "- [ ] Social Login (Google, Facebook) - Status: Postponed from MVP"
    
    update_modules_breakdown_table:
      find_row: "| Auth - Social | MVP | Should | 0% | Not Started |"
      change_to: "| Auth - Social | Phase 1 | Should | 0% | Postponed | [new date] |"
    
    recalculate_completion:
      mvp_features: 9 → 8
      mvp_completed: 3
      new_completion: 3/8 = 37.5% (was 3/9 = 33%)
      progress_increased: true (scope reduction)
    
    update_timeline:
      if_removes_bottleneck:
        - Recalculate MVP end date
        - May finish earlier
        - Update milestones
    
    version: MINOR bump (1.3 → 1.4)
    
    changelog: |
      ### v1.4 - [date]
      - Changed: Social Login moved from MVP to Phase 1
      - Impact: MVP scope reduced by 5-7 days
      - Timeline: MVP back on track for [date]
      - Reason: Prioritizing core functionality
  
  Step 3.3: Update Module Requirements
    file: /MODULES_REQUIREMENTS/auth_requirements.md
    
    find_social_login_requirements:
      sections:
        - FR-AUTH-008: Google OAuth Integration
        - FR-AUTH-009: Facebook OAuth Integration
        - FR-AUTH-010: Social Account Linking
    
    action: ADD_POSTPONED_NOTE (don't delete)
    
    add_at_top_of_each_FR:
      
⚠️ **STATUS: POSTPONED TO PHASE 1**
      Originally planned for MVP, moved to Phase 1 on [date].
      Reason: Timeline optimization.
      Implementation deferred but requirements remain valid.

    
    alternative_action: MOVE_TO_SEPARATE_SECTION
      create_section: "## FUTURE REQUIREMENTS (Phase 1+)"
      move_frs_there: [FR-AUTH-008, FR-AUTH-009, FR-AUTH-010]
      
      keep_note:
        
These requirements were originally planned for MVP but 
        moved to Phase 1 to maintain timeline. They remain valid 
        and ready for implementation.

    
    version: PATCH bump (1.1.0 → 1.1.1)
    
    changelog: |
      ### v1.1.1 - [date]
      - Postponed: FR-AUTH-008, 009, 010 (Social Login)
      - Moved to: Phase 1
      - Status: Requirements remain valid, implementation deferred
      - No changes to existing implemented FRs
  
  Step 3.4: Update Context
    file: /CONTEXT_MEMORY/decisions.md
    
    add_entry: |
      ## DEC-043: Remove Social Login from MVP Scope
      **Date:** [today]
      **Status:** Approved
      **Category:** Scope Reduction
      **Impact:** MEDIUM
      
      **Context:**
      MVP timeline at risk due to accumulated scope. Team identified 
      features that could be safely deferred to maintain quality of 
      core functionality.
      
      **Decision:**
      Remove Social Login (Google/Facebook OAuth) from MVP scope. 
      Move to Phase 1 instead.
      
      **Rationale:**
      - MVP timeline pressure (behind by 1 week)
      - Social Login is "Should Have", not "Must Have"
      - Core auth (email/password) sufficient for MVP
      - No features depend on Social Login
      - Can be added in Phase 1 without issues
      - Saves 5-7 days of development time
      
      **Alternatives Considered:**
      - Extend MVP timeline: Rejected (business constraints)
      - Cut different feature: Evaluated (Social Login best choice)
      - Implement minimal version: Rejected (half-done feature worse)
      
      **Impact:**
      **Positive:**
      - MVP timeline preserved
      - Team pressure reduced
      - Focus on core features
      - Quality maintained
      
      **Negative:**
      - Slightly less convenient signup
      - Some users may prefer social login
      - Acceptable trade-off for timely MVP
      
      **User Impact:**
      - Users can still sign up/login with email
      - Social login available in Phase 1
      - No core functionality lost
      
      **Timeline:**
      - Freed up: 5-7 days
      - MVP completion: On track for [date]
      - Social Login in Phase 1: [date]
      
      **Rollback Plan:**
      If MVP finishes early AND team has capacity:
      - Can add back to MVP before launch
      - Requirements ready
      - Low risk
      
      **Communication:**
      - Inform stakeholders: Yes
      - Update product roadmap: Yes
      - User communication: Not needed (pre-launch)
      
      **References:**
      - PRD v1.7 - Section 4.7
      - ROADMAP v1.4
      - auth_requirements.md v1.1.1
      - Original estimate: DEC-015
    
    file: /CONTEXT_MEMORY/state.md
    
    update_section: "## RECENT DECISIONS"
    add_line: |
      - [Date]: Removed Social Login from MVP scope (moved to Phase 1)
                Timeline preserved, MVP back on track
    
    if_affects_current_work:
      update_section: "## NEXT STEPS"
      remove_item: "- [ ] Implement Social Login"
      replace_with: "- [ ] [Next priority item]"
  
  Step 3.5: Update Progress Tracking
    file: /PROGRESS_TRACKING/modules_status.md
    
    find_row: "| Auth - Social | MVP | Should | 0% | Not Started |"
    
    update_to: "| Auth - Social | Phase 1 | Should | 0% | Postponed | [new target] | Moved from MVP |"
    
    recalculate_progress:
      mvp_scope: -5-7 days
      overall_completion: may increase (fewer items)
    
    add_to_recent_updates: |
      - [Date]: ⚠️ Social Login removed from MVP, moved to Phase 1
                Reason: Timeline optimization
                Impact: MVP scope reduced, timeline preserved
    
    file: /PROGRESS_TRACKING/backlog.md
    
    if_has_detailed_backlog:
      find_or_create_section: "## PHASE 1 PRIORITIES"
      
      add_item: |
        - [ ] **Social Login** (moved from MVP)
          - Google OAuth integration
          - Facebook OAuth integration
          - Account linking
          - Priority: Should Have
          - Estimate: 5-7 days
          - Deferred from MVP for timeline reasons

PHASE 4: CODE CLEANUP (if applicable)
  
  Step 4.1: Check for Existing Code
    if_no_code:
      skip_this_phase: true
    
    if_partial_code:
      identify_files:
        - Controllers: auth/socialController.js
        - Routes: auth/socialRoutes.js
        - Services: auth/googleAuth.js, auth/facebookAuth.js
        - Frontend: components/SocialLoginButtons.jsx
        - Tests: auth/social.test.js
      
      action_options:
        option_1_remove:
          - Delete files
          - Remove from git

# Best Practice (Bp Premier) — research sheet

**Confidence:** vendor + official KB = good. Independent GP reviews: searches returned none usable (Capterra hits were a different "Premier"; no Reddit/forum threads surfaced). "Clumsy" points below are therefore partly *inferred from the documented workflow*, flagged `[inferred]`. YouTube transcripts not retrievable with the tools here; to be verified with the client's BP screenshots.

## Layout and navigation model
- Windows desktop app on Microsoft SQL Server, server-based, on-premise. Many separate windows: Main screen, Appointment book, Waiting room, Patient list, Open patient (F2), Patient record, Inbox, Follow-Up Inbox. F10 opens Patient list, F2 Open patient. Keyboard shortcuts are a headline efficiency feature.
- Reception flow: Book -> Arrive (check Medicare details, mark ready) -> Waiting room (automatic) -> Start visit (double-click / button / right-click / F2 in waiting room) -> Finalise visit (generates invoice items, appointment set to "At billing") -> Invoice -> Paid -> Complete.

## Hero-screen anatomy (Appointment book)
Time grid per provider; slot/appointment colour = status. Documented statuses: Unavailable, On the day, Waiting (yellow), With Doctor, At billing, Invoiced, Paid, Completed, Did not attend, Urgent (overrides colour), Elsewhere. Colours cannot be customised. Reminder replies shown as green/red/yellow dots.

## Key features
Appointment book + Best Health Booking (online, real-time sync, after-hours); Bp Comms SMS (two-way YES confirm, dedicated AU number); results (pathology, radiology, cytology) to practitioner Inbox; Follow-Up Inbox; clinical decision support; Lyrebird Scribe (generative AI note-taking); role-based permissions; scheduled backups; monthly drug + billing data updates; Medicare online claiming (direct bill, patient claiming, EasyClaim/Tyro); Partner Network 200+ integrations; Bp Mobile; KB with 1,000+ articles + paid courses. Claims 7,000+ practices, 27,000+ professionals. Current news: Oxford SP1 (security hardening), AoB reform from 1 Jul 2026, SMS Sender ID register from 1 Jul 2026.

## What users praise (vendor/KB-side)
Stability and familiarity, large training ecosystem, deep Australian billing/clinical coverage, keyboard shortcuts, status-driven workflow.

## "Clumsy" points
- `[inferred]` Status is a colour legend that can't be customised; legend needs learning; "Invoiced/Paid" hidden behind a setting.
- `[inferred]` Workflow spread across many windows (book, waiting room, record, inbox, follow-up inbox); each is a separate window to juggle.
- Halaxy's competing blog calls BP/MD "designed when general practice looked very different", server/IT overhead, periodic paid updates, fragmented data, add-on AI (vendor-biased, unsourced).
- Tension with the client's own findings: BP shows *actions* (Send to AIR, View AIR) but local-saved vs sent vs acknowledged is not the headline state.

## Integrations
Medicare online claiming, Best Health Booking, Bp Comms, Lyrebird, Partner Network. AIR/eRx/MHR are standard in BP but not itemised on the pages fetched.

## Sources
- https://bestpracticesoftware.com/landing-page-bp-premier-main
- https://kb.bpsoftware.net/bppremier/oxford/Management/AppointmentBook/ApptStatuses.htm
- https://kb.bpsoftware.net/bppremier/oxford/GettingStarted/Reception.htm
- https://kb.bpsoftware.net/bppremier/latestnews/index.htm
- https://kb.bpsoftware.net/au/bppremier/jade/Content/Management/AppointmentBook/AppointmentBookWorkflow.htm (via search summary)
- https://blog.halaxy.com/best-practice-vs-medical-director-vs-halaxy-why-australian-gps-are-choosing-a-new-foundation-for-their-practice/ (competitor claim)

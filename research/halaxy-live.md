# Halaxy live product study (read-only, 27 Oct 2026)

**How:** the user's own signed-in test account, in the built-in browser. Only opened pages, a dropdown and hover menus. Nothing was submitted, created, sent or changed. No credentials were typed. Patient data in the account was a test record and is not reproduced here. This is a behaviour and layout note, not a copy brief: no wording, icons or colours are reused.

## Shell and navigation
- Narrow dark icon rail on the left. On hover it expands into a labelled menu with collapsible groups: Patients (Patient List, Add Patient), Schedule, Finances, Reports, Contacts, Personal, Settings, plus a "Help and resources" footer. Icons alone are not labelled until hover (discoverability cost, big gain in screen width).
- Top bar: record-type selector ("Patient") joined to a search box (name, email, phone, patient id), then inbox, notifications, chat, avatar.
- A banner asks the user to verify their profile to unlock features. A floating round "book" button bottom-left opens help.
- A gradient sparkle button sits top-right on pages (AI entry point). Inside a note it also appears as "Summarise notes" in the Actions menu.

## Calendar (hero)
- Toolbar: Today, This week, a Week dropdown (day/week/month), previous and next, a timezone label, a Multilocation dropdown, zoom in, zoom out, a "my calendar" toggle, search, refresh, print, settings.
- Time grid is 15-minute rows over 24 hours, today's column header tinted. Appointments are blocks with start-end time, patient name and a small payment label.
- Clicking an appointment goes straight to that patient's Clinical Notes tab. The payment label ("$") on the block jumps to that appointment's invoice instead. So one block has two destinations.
- No drawer: the calendar leaves for a full page for notes and invoices.

## Patient record
- Tabs: General, Clinical Notes, Clinical Dashboard, Funding, Invoices, Appointments, Social History.
- Header actions: Add appointment, New clinical note (primary), Actions menu: print preview, print, email, preferences, share notes, summarise notes (AI).
- A notes menu (search, filter, sort, settings) above note cards. A note card shows a status badge (Published), publish time, revert, links to its appointment and its invoice, attach file.
- A floating right-hand strip with Patient, History, Favourites, Settings shortcuts.

## Invoice page
- Header: invoice number, patient, status badge (Paid in full), icons for list, attach, print, send.
- Cards: practitioner details (edit), patient details with a patient-claim block (member number, add referral), fees and charges table (date, item code, description, tax, total) with "add another fee".

## What this means for the PMS Halaxy variant
Kept from ours: calendar with drawer (stays on the calendar), AIR and My Health Record states, the integration status block.
Borrowed as ideas, built our own way:
1. Icon rail that expands on hover, with a pin toggle. Frees width for the calendar.
2. Calendar zoom (row height) as a toolbar control.
3. Payment state visible on the appointment block, with a direct route to the invoice from the drawer.
4. AI actions always labelled and gated, never one-click into the record.
Not copied: 24-hour grid, full-page jump away from the calendar, unlabelled icons without a tooltip.

## Gaps seen
No AIR, My Health Record, eRx or results-inbox surface was visible on the calendar or record screens I opened. Only the account's menus were skimmed, so this is not proof they do not exist elsewhere.

## Second pass (patient list, finances, menu), read-only
- **Menu tree (expanded):** Patients (Patient List, Add Patient); Schedule (Calendar, Appointment List, Waiting List, Tasks and Follow-Ups); Finances (Expenses, Invoices, Fees, Discounts); Reports; Contacts; Personal; Settings; Help and resources. Groups collapse; the current item is tinted.
- **Patient list:** a data grid, not cards. Header: title, primary Add Patient, Export and Print dropdown, keyword search, Layout (distribute equally / normal), rows per page (50), a side "Columns" tab to show or hide columns, first/prev/next/last paging. Available columns: label, primary contact, preferred name, given name, surname, created, status, date of birth, patient number, email, phone, last appointment (with attended state), next appointment, address, location, review date, review notes.
- **Fees page (finance setup):** tab strip Fees, Funders, Identifications, Referral Types, Products, Packages, Invoice Schedules; New Fee and Export and Print; a grid with funder, fee number and name, category, type, duration, amount, tax, total, rebate, status, express, visibility, booking payment, location type.
- **Invoice** (from the first pass): number, patient, status badge, fees and charges table.
- **Reports:** the menu group exists, but my clicks landed on other pages, so I did not open any report. Report names come from the earlier screenshot notes in `/home/shajib/Documents/PMS/docs/halaxy-analysis.md` (Finance, Medicare, Patient, Appointment, Contact, Communication, Clinical, Practice Dashboard, Surveys), not from this session.

## Decision: the Halaxy variant now mirrors /home/shajib/Documents/PMS
By request, `toolii-vs-halaxy.html` follows the user's own PMS build instead of Halaxy's visuals: the same oklch tokens (warm paper, one purple signal), Schibsted Grotesk, Instrument Sans and DM Mono (embedded, SIL OFL), the inset paper rail with collapsible groups and a white tile for the current page, the 64px top bar with a pill search, command button and New patient, the Today screen (greeting, day-pulse bar, quick-link pills, schedule timeline with a Now marker, purple Up next card, Unfinished, Tasks) and a calendar with open hours white, closed hours grey and a docked 22rem panel. From Halaxy itself only behaviour ideas remain (patient list as a column grid with export, invoice reachable from the appointment). The detector's "cream background" note is the PMS paper tone, kept on purpose.

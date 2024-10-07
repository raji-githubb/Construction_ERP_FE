from django.urls import path
from .views import *

urlpatterns = [
    path("",login, name="login"),
    path("dashboard/",dashboard, name="dashboard"),
    #add here fron-end urls

    

    path('user/', user_create, name='user'),
    path('user-view/<pk>/', user_view, name='user_view'),
    path('user-edit/<pk>/', user_edit, name='user_edit'),
    path('user-delete/<pk>/', user_delete, name='user_delete'),

    path('assetcategory/', assetcategory_create, name='assetcategory'),
    path('assetcategory-view/<pk>/', assetcategory_view, name='assetcategory_view'),
    path('assetcategory-edit/<pk>/', assetcategory_edit, name='assetcategory_edit'),
    path('assetcategory-delete/<pk>/', assetcategory_delete, name='assetcategory_delete'),

    path('warehouse/', warehouse_create, name='warehouse'),
    path('warehouse-view/<pk>/', warehouse_view, name='warehouse_view'),
    path('warehouse-edit/<pk>/', warehouse_edit, name='warehouse_edit'),
    path('warehouse-delete/<pk>/', warehouse_delete, name='warehouse_delete'),

    path('subcontractor/', subcontractor_create, name='subcontractor'),
    path('subcontractor-view/<pk>/', subcontractor_view, name='subcontractor_view'),
    path('subcontractor-edit/<pk>/', subcontractor_edit, name='subcontractor_edit'),
    path('subcontractor-delete/<pk>/', subcontractor_delete, name='subcontractor_delete'),

    path('opportunityidentification/', opportunityidentification_create, name='opportunityidentification'),
    path('opportunityidentification-view/<pk>/', opportunityidentification_view, name='opportunityidentification_view'),
    path('opportunityidentification-edit/<pk>/', opportunityidentification_edit, name='opportunityidentification_edit'),
    path('opportunityidentification-delete/<pk>/', opportunityidentification_delete, name='opportunityidentification_delete'),

    path('bidproposal/', bidproposal_create, name='bidproposal'),
    path('bidproposal-view/<pk>/', bidproposal_view, name='bidproposal_view'),
    path('bidproposal-edit/<pk>/', bidproposal_edit, name='bidproposal_edit'),
    path('bidproposal-delete/<pk>/', bidproposal_delete, name='bidproposal_delete'),

    path('currency/', currency_create, name='currency'),
    path('currency-view/<pk>/', currency_view, name='currency_view'),
    path('currency-edit/<pk>/', currency_edit, name='currency_edit'),
    path('currency-delete/<pk>/', currency_delete, name='currency_delete'),

    path('clientinteractiontype/', clientinteractiontype_create, name='clientinteractiontype'),
    path('clientinteractiontype-view/<pk>/', clientinteractiontype_view, name='clientinteractiontype_view'),
    path('clientinteractiontype-edit/<pk>/', clientinteractiontype_edit, name='clientinteractiontype_edit'),
    path('clientinteractiontype-delete/<pk>/', clientinteractiontype_delete, name='clientinteractiontype_delete'),

    path('costcategory/', costcategory_create, name='costcategory'),
    path('costcategory-view/<pk>/', costcategory_view, name='costcategory_view'),
    path('costcategory-edit/<pk>/', costcategory_edit, name='costcategory_edit'),
    path('costcategory-delete/<pk>/', costcategory_delete, name='costcategory_delete'),

    path('equipmentcategory/', equipmentcategory_create, name='equipmentcategory'),
    path('equipmentcategory-view/<pk>/', equipmentcategory_view, name='equipmentcategory_view'),
    path('equipmentcategory-edit/<pk>/', equipmentcategory_edit, name='equipmentcategory_edit'),
    path('equipmentcategory-delete/<pk>/', equipmentcategory_delete, name='equipmentcategory_delete'),

    path('account/', account_create, name='account'),
    path('account-view/<pk>/', account_view, name='account_view'),
    path('account-edit/<pk>/', account_edit, name='account_edit'),
    path('account-delete/<pk>/', account_delete, name='account_delete'),

    path('itemcategory/', itemcategory_create, name='itemcategory'),
    path('itemcategory-view/<pk>/', itemcategory_view, name='itemcategory_view'),
    path('itemcategory-edit/<pk>/', itemcategory_edit, name='itemcategory_edit'),
    path('itemcategory-delete/<pk>/', itemcategory_delete, name='itemcategory_delete'),

    path('supplier/', supplier_create, name='supplier'),
    path('supplier-view/<pk>/', supplier_view, name='supplier_view'),
    path('supplier-edit/<pk>/', supplier_edit, name='supplier_edit'),
    path('supplier-delete/<pk>/', supplier_delete, name='supplier_delete'),

    path('leadsource/', leadsource_create, name='leadsource'),
    path('leadsource-view/<pk>/', leadsource_view, name='leadsource_view'),
    path('leadsource-edit/<pk>/', leadsource_edit, name='leadsource_edit'),
    path('leadsource-delete/<pk>/', leadsource_delete, name='leadsource_delete'),

    path('salesrepresentative/', salesrepresentative_create, name='salesrepresentative'),
    path('salesrepresentative-view/<pk>/', salesrepresentative_view, name='salesrepresentative_view'),
    path('salesrepresentative-edit/<pk>/', salesrepresentative_edit, name='salesrepresentative_edit'),
    path('salesrepresentative-delete/<pk>/', salesrepresentative_delete, name='salesrepresentative_delete'),

    path('riskowner/', riskowner_create, name='riskowner'),
    path('riskowner-view/<pk>/', riskowner_view, name='riskowner_view'),
    path('riskowner-edit/<pk>/', riskowner_edit, name='riskowner_edit'),
    path('riskowner-delete/<pk>/', riskowner_delete, name='riskowner_delete'),

    path('salesstage/', salesstage_create, name='salesstage'),
    path('salesstage-view/<pk>/', salesstage_view, name='salesstage_view'),
    path('salesstage-edit/<pk>/', salesstage_edit, name='salesstage_edit'),
    path('salesstage-delete/<pk>/', salesstage_delete, name='salesstage_delete'),

    path('customer/', customer_create, name='customer'),
    path('customer-view/<pk>/', customer_view, name='customer_view'),
    path('customer-edit/<pk>/', customer_edit, name='customer_edit'),
    path('customer-delete/<pk>/', customer_delete, name='customer_delete'),

    path('riskcategory/', riskcategory_create, name='riskcategory'),
    path('riskcategory-view/<pk>/', riskcategory_view, name='riskcategory_view'),
    path('riskcategory-edit/<pk>/', riskcategory_edit, name='riskcategory_edit'),
    path('riskcategory-delete/<pk>/', riskcategory_delete, name='riskcategory_delete'),

    path('contractor/', contractor_create, name='contractor'),
    path('contractor-view/<pk>/', contractor_view, name='contractor_view'),
    path('contractor-edit/<pk>/', contractor_edit, name='contractor_edit'),
    path('contractor-delete/<pk>/', contractor_delete, name='contractor_delete'),

    path('delaycause/', delaycause_create, name='delaycause'),
    path('delaycause-view/<pk>/', delaycause_view, name='delaycause_view'),
    path('delaycause-edit/<pk>/', delaycause_edit, name='delaycause_edit'),
    path('delaycause-delete/<pk>/', delaycause_delete, name='delaycause_delete'),

    path('individual/', individual_create, name='individual'),
    path('individual-view/<pk>/', individual_view, name='individual_view'),
    path('individual-edit/<pk>/', individual_edit, name='individual_edit'),
    path('individual-delete/<pk>/', individual_delete, name='individual_delete'),

    path('internaldepartment/', internaldepartment_create, name='internaldepartment'),
    path('internaldepartment-view/<pk>/', internaldepartment_view, name='internaldepartment_view'),
    path('internaldepartment-edit/<pk>/', internaldepartment_edit, name='internaldepartment_edit'),
    path('internaldepartment-delete/<pk>/', internaldepartment_delete, name='internaldepartment_delete'),

    path('project/', project_create, name='project'),
    path('project-view/<pk>/', project_view, name='project_view'),
    path('project-edit/<pk>/', project_edit, name='project_edit'),
    path('project-delete/<pk>/', project_delete, name='project_delete'),

    path('resource/', resource_create, name='resource'),
    path('resource-view/<pk>/', resource_view, name='resource_view'),
    path('resource-edit/<pk>/', resource_edit, name='resource_edit'),
    path('resource-delete/<pk>/', resource_delete, name='resource_delete'),

    path('rfprfq/', rfprfq_create, name='rfprfq'),
    path('rfprfq-view/<pk>/', rfprfq_view, name='rfprfq_view'),
    path('rfprfq-edit/<pk>/', rfprfq_edit, name='rfprfq_edit'),
    path('rfprfq-delete/<pk>/', rfprfq_delete, name='rfprfq_delete'),

    path('role/', role_create, name='role'),
    path('role-view/<pk>/', role_view, name='role_view'),
    path('role-edit/<pk>/', role_edit, name='role_edit'),
    path('role-delete/<pk>/', role_delete, name='role_delete'),

    path('scoringcriteria/', scoringcriteria_create, name='scoringcriteria'),
    path('scoringcriteria-view/<pk>/', scoringcriteria_view, name='scoringcriteria_view'),
    path('scoringcriteria-edit/<pk>/', scoringcriteria_edit, name='scoringcriteria_edit'),
    path('scoringcriteria-delete/<pk>/', scoringcriteria_delete, name='scoringcriteria_delete'),

    path('taskcategory/', taskcategory_create, name='taskcategory'),
    path('taskcategory-view/<pk>/', taskcategory_view, name='taskcategory_view'),
    path('taskcategory-edit/<pk>/', taskcategory_edit, name='taskcategory_edit'),
    path('taskcategory-delete/<pk>/', taskcategory_delete, name='taskcategory_delete'),

    path('taskdurationestimation/', taskdurationestimation_create, name='taskdurationestimation'),
    path('taskdurationestimation-view/<pk>/', taskdurationestimation_view, name='taskdurationestimation_view'),
    path('taskdurationestimation-edit/<pk>/', taskdurationestimation_edit, name='taskdurationestimation_edit'),
    path('taskdurationestimation-delete/<pk>/', taskdurationestimation_delete, name='taskdurationestimation_delete'),

    path('taskpriority/', taskpriority_create, name='taskpriority'),
    path('taskpriority-view/<pk>/', taskpriority_view, name='taskpriority_view'),
    path('taskpriority-edit/<pk>/', taskpriority_edit, name='taskpriority_edit'),
    path('taskpriority-delete/<pk>/', taskpriority_delete, name='taskpriority_delete'),

    path('team/', team_create, name='team'),
    path('team-view/<pk>/', team_view, name='team_view'),
    path('team-edit/<pk>/', team_edit, name='team_edit'),
    path('team-delete/<pk>/', team_delete, name='team_delete'),

    path('vendor/', vendor_create, name='vendor'),
    path('vendor-view/<pk>/', vendor_view, name='vendor_view'),
    path('vendor-edit/<pk>/', vendor_edit, name='vendor_edit'),
    path('vendor-delete/<pk>/', vendor_delete, name='vendor_delete'),

    path('asset/', asset_create, name='asset'),
    path('asset-view/<pk>/', asset_view, name='asset_view'),
    path('asset-edit/<pk>/', asset_edit, name='asset_edit'),
    path('asset-delete/<pk>/', asset_delete, name='asset_delete'),

    path('expertise/', expertise_create, name='expertise'),
    path('expertise-view/<pk>/', expertise_view, name='expertise_view'),
    path('expertise-edit/<pk>/', expertise_edit, name='expertise_edit'),
    path('expertise-delete/<pk>/', expertise_delete, name='expertise_delete'),

    path('bidnobiddecision/', bidnobiddecision_create, name='bidnobiddecision'),
    path('bidnobiddecision-view/<pk>/', bidnobiddecision_view, name='bidnobiddecision_view'),
    path('bidnobiddecision-edit/<pk>/', bidnobiddecision_edit, name='bidnobiddecision_edit'),
    path('bidnobiddecision-delete/<pk>/', bidnobiddecision_delete, name='bidnobiddecision_delete'),

    path('proposalpreparation/', proposalpreparation_create, name='proposalpreparation'),
    path('proposalpreparation-view/<pk>/', proposalpreparation_view, name='proposalpreparation_view'),
    path('proposalpreparation-edit/<pk>/', proposalpreparation_edit, name='proposalpreparation_edit'),
    path('proposalpreparation-delete/<pk>/', proposalpreparation_delete, name='proposalpreparation_delete'),

    path('bidsubmission/', bidsubmission_create, name='bidsubmission'),
    path('bidsubmission-view/<pk>/', bidsubmission_view, name='bidsubmission_view'),
    path('bidsubmission-edit/<pk>/', bidsubmission_edit, name='bidsubmission_edit'),
    path('bidsubmission-delete/<pk>/', bidsubmission_delete, name='bidsubmission_delete'),

    path('equipment/', equipment_create, name='equipment'),
    path('equipment-view/<pk>/', equipment_view, name='equipment_view'),
    path('equipment-edit/<pk>/', equipment_edit, name='equipment_edit'),
    path('equipment-delete/<pk>/', equipment_delete, name='equipment_delete'),

    path('notification/', notification_create, name='notification'),
    path('notification-view/<pk>/', notification_view, name='notification_view'),
    path('notification-edit/<pk>/', notification_edit, name='notification_edit'),
    path('notification-delete/<pk>/', notification_delete, name='notification_delete'),

    path('item/', item_create, name='item'),
    path('item-view/<pk>/', item_view, name='item_view'),
    path('item-edit/<pk>/', item_edit, name='item_edit'),
    path('item-delete/<pk>/', item_delete, name='item_delete'),

    path('lead/', lead_create, name='lead'),
    path('lead-view/<pk>/', lead_view, name='lead_view'),
    path('lead-edit/<pk>/', lead_edit, name='lead_edit'),
    path('lead-delete/<pk>/', lead_delete, name='lead_delete'),

    path('procurementneed/', procurementneed_create, name='procurementneed'),
    path('procurementneed-view/<pk>/', procurementneed_view, name='procurementneed_view'),
    path('procurementneed-edit/<pk>/', procurementneed_edit, name='procurementneed_edit'),
    path('procurementneed-delete/<pk>/', procurementneed_delete, name='procurementneed_delete'),

    path('audit/', audit_create, name='audit'),
    path('audit-view/<pk>/', audit_view, name='audit_view'),
    path('audit-edit/<pk>/', audit_edit, name='audit_edit'),
    path('audit-delete/<pk>/', audit_delete, name='audit_delete'),

    path('bid/', bid_create, name='bid'),
    path('bid-view/<pk>/', bid_view, name='bid_view'),
    path('bid-edit/<pk>/', bid_edit, name='bid_edit'),
    path('bid-delete/<pk>/', bid_delete, name='bid_delete'),

    path('budget/', budget_create, name='budget'),
    path('budget-view/<pk>/', budget_view, name='budget_view'),
    path('budget-edit/<pk>/', budget_edit, name='budget_edit'),
    path('budget-delete/<pk>/', budget_delete, name='budget_delete'),

    path('budgetallocation/', budgetallocation_create, name='budgetallocation'),
    path('budgetallocation-view/<pk>/', budgetallocation_view, name='budgetallocation_view'),
    path('budgetallocation-edit/<pk>/', budgetallocation_edit, name='budgetallocation_edit'),
    path('budgetallocation-delete/<pk>/', budgetallocation_delete, name='budgetallocation_delete'),

    path('clientfeedback/', clientfeedback_create, name='clientfeedback'),
    path('clientfeedback-view/<pk>/', clientfeedback_view, name='clientfeedback_view'),
    path('clientfeedback-edit/<pk>/', clientfeedback_edit, name='clientfeedback_edit'),
    path('clientfeedback-delete/<pk>/', clientfeedback_delete, name='clientfeedback_delete'),

    path('clientfollowup/', clientfollowup_create, name='clientfollowup'),
    path('clientfollowup-view/<pk>/', clientfollowup_view, name='clientfollowup_view'),
    path('clientfollowup-edit/<pk>/', clientfollowup_edit, name='clientfollowup_edit'),
    path('clientfollowup-delete/<pk>/', clientfollowup_delete, name='clientfollowup_delete'),

    path('clientsatisfactionsurvey/', clientsatisfactionsurvey_create, name='clientsatisfactionsurvey'),
    path('clientsatisfactionsurvey-view/<pk>/', clientsatisfactionsurvey_view, name='clientsatisfactionsurvey_view'),
    path('clientsatisfactionsurvey-edit/<pk>/', clientsatisfactionsurvey_edit, name='clientsatisfactionsurvey_edit'),
    path('clientsatisfactionsurvey-delete/<pk>/', clientsatisfactionsurvey_delete, name='clientsatisfactionsurvey_delete'),

    path('closeoutdocument/', closeoutdocument_create, name='closeoutdocument'),
    path('closeoutdocument-view/<pk>/', closeoutdocument_view, name='closeoutdocument_view'),
    path('closeoutdocument-edit/<pk>/', closeoutdocument_edit, name='closeoutdocument_edit'),
    path('closeoutdocument-delete/<pk>/', closeoutdocument_delete, name='closeoutdocument_delete'),

    path('compliancemonitor/', compliancemonitor_create, name='compliancemonitor'),
    path('compliancemonitor-view/<pk>/', compliancemonitor_view, name='compliancemonitor_view'),
    path('compliancemonitor-edit/<pk>/', compliancemonitor_edit, name='compliancemonitor_edit'),
    path('compliancemonitor-delete/<pk>/', compliancemonitor_delete, name='compliancemonitor_delete'),

    path('contract/', contract_create, name='contract'),
    path('contract-view/<pk>/', contract_view, name='contract_view'),
    path('contract-edit/<pk>/', contract_edit, name='contract_edit'),
    path('contract-delete/<pk>/', contract_delete, name='contract_delete'),

    path('contractawardexecution/', contractawardexecution_create, name='contractawardexecution'),
    path('contractawardexecution-view/<pk>/', contractawardexecution_view, name='contractawardexecution_view'),
    path('contractawardexecution-edit/<pk>/', contractawardexecution_edit, name='contractawardexecution_edit'),
    path('contractawardexecution-delete/<pk>/', contractawardexecution_delete, name='contractawardexecution_delete'),

    path('costestimation/', costestimation_create, name='costestimation'),
    path('costestimation-view/<pk>/', costestimation_view, name='costestimation_view'),
    path('costestimation-edit/<pk>/', costestimation_edit, name='costestimation_edit'),
    path('costestimation-delete/<pk>/', costestimation_delete, name='costestimation_delete'),

    path('finalclientsignoff/', finalclientsignoff_create, name='finalclientsignoff'),
    path('finalclientsignoff-view/<pk>/', finalclientsignoff_view, name='finalclientsignoff_view'),
    path('finalclientsignoff-edit/<pk>/', finalclientsignoff_edit, name='finalclientsignoff_edit'),
    path('finalclientsignoff-delete/<pk>/', finalclientsignoff_delete, name='finalclientsignoff_delete'),

    path('finalinspection/', finalinspection_create, name='finalinspection'),
    path('finalinspection-view/<pk>/', finalinspection_view, name='finalinspection_view'),
    path('finalinspection-edit/<pk>/', finalinspection_edit, name='finalinspection_edit'),
    path('finalinspection-delete/<pk>/', finalinspection_delete, name='finalinspection_delete'),

    path('finalreview/', finalreview_create, name='finalreview'),
    path('finalreview-view/<pk>/', finalreview_view, name='finalreview_view'),
    path('finalreview-edit/<pk>/', finalreview_edit, name='finalreview_edit'),
    path('finalreview-delete/<pk>/', finalreview_delete, name='finalreview_delete'),

    path('financialtransaction/', financialtransaction_create, name='financialtransaction'),
    path('financialtransaction-view/<pk>/', financialtransaction_view, name='financialtransaction_view'),
    path('financialtransaction-edit/<pk>/', financialtransaction_edit, name='financialtransaction_edit'),
    path('financialtransaction-delete/<pk>/', financialtransaction_delete, name='financialtransaction_delete'),

    path('incidentreport/', incidentreport_create, name='incidentreport'),
    path('incidentreport-view/<pk>/', incidentreport_view, name='incidentreport_view'),
    path('incidentreport-edit/<pk>/', incidentreport_edit, name='incidentreport_edit'),
    path('incidentreport-delete/<pk>/', incidentreport_delete, name='incidentreport_delete'),

    path('inspection/', inspection_create, name='inspection'),
    path('inspection-view/<pk>/', inspection_view, name='inspection_view'),
    path('inspection-edit/<pk>/', inspection_edit, name='inspection_edit'),
    path('inspection-delete/<pk>/', inspection_delete, name='inspection_delete'),

    path('legalrequirement/', legalrequirement_create, name='legalrequirement'),
    path('legalrequirement-view/<pk>/', legalrequirement_view, name='legalrequirement_view'),
    path('legalrequirement-edit/<pk>/', legalrequirement_edit, name='legalrequirement_edit'),
    path('legalrequirement-delete/<pk>/', legalrequirement_delete, name='legalrequirement_delete'),

    path('message/', message_create, name='message'),
    path('message-view/<pk>/', message_view, name='message_view'),
    path('message-edit/<pk>/', message_edit, name='message_edit'),
    path('message-delete/<pk>/', message_delete, name='message_delete'),

    path('milestone/', milestone_create, name='milestone'),
    path('milestone-view/<pk>/', milestone_view, name='milestone_view'),
    path('milestone-edit/<pk>/', milestone_edit, name='milestone_edit'),
    path('milestone-delete/<pk>/', milestone_delete, name='milestone_delete'),

    path('milestonebilling/', milestonebilling_create, name='milestonebilling'),
    path('milestonebilling-view/<pk>/', milestonebilling_view, name='milestonebilling_view'),
    path('milestonebilling-edit/<pk>/', milestonebilling_edit, name='milestonebilling_edit'),
    path('milestonebilling-delete/<pk>/', milestonebilling_delete, name='milestonebilling_delete'),

    path('payroll/', payroll_create, name='payroll'),
    path('payroll-view/<pk>/', payroll_view, name='payroll_view'),
    path('payroll-edit/<pk>/', payroll_edit, name='payroll_edit'),
    path('payroll-delete/<pk>/', payroll_delete, name='payroll_delete'),

    path('postprojectreview/', postprojectreview_create, name='postprojectreview'),
    path('postprojectreview-view/<pk>/', postprojectreview_view, name='postprojectreview_view'),
    path('postprojectreview-edit/<pk>/', postprojectreview_edit, name='postprojectreview_edit'),
    path('postprojectreview-delete/<pk>/', postprojectreview_delete, name='postprojectreview_delete'),

    path('projectcloseout/', projectcloseout_create, name='projectcloseout'),
    path('projectcloseout-view/<pk>/', projectcloseout_view, name='projectcloseout_view'),
    path('projectcloseout-edit/<pk>/', projectcloseout_edit, name='projectcloseout_edit'),
    path('projectcloseout-delete/<pk>/', projectcloseout_delete, name='projectcloseout_delete'),

    path('projectcommunication/', projectcommunication_create, name='projectcommunication'),
    path('projectcommunication-view/<pk>/', projectcommunication_view, name='projectcommunication_view'),
    path('projectcommunication-edit/<pk>/', projectcommunication_edit, name='projectcommunication_edit'),
    path('projectcommunication-delete/<pk>/', projectcommunication_delete, name='projectcommunication_delete'),

    path('projectdocumentation/', projectdocumentation_create, name='projectdocumentation'),
    path('projectdocumentation-view/<pk>/', projectdocumentation_view, name='projectdocumentation_view'),
    path('projectdocumentation-edit/<pk>/', projectdocumentation_edit, name='projectdocumentation_edit'),
    path('projectdocumentation-delete/<pk>/', projectdocumentation_delete, name='projectdocumentation_delete'),

    path('projectfinancialcloseout/', projectfinancialcloseout_create, name='projectfinancialcloseout'),
    path('projectfinancialcloseout-view/<pk>/', projectfinancialcloseout_view, name='projectfinancialcloseout_view'),
    path('projectfinancialcloseout-edit/<pk>/', projectfinancialcloseout_edit, name='projectfinancialcloseout_edit'),
    path('projectfinancialcloseout-delete/<pk>/', projectfinancialcloseout_delete, name='projectfinancialcloseout_delete'),

    path('projectperformancereview/', projectperformancereview_create, name='projectperformancereview'),
    path('projectperformancereview-view/<pk>/', projectperformancereview_view, name='projectperformancereview_view'),
    path('projectperformancereview-edit/<pk>/', projectperformancereview_edit, name='projectperformancereview_edit'),
    path('projectperformancereview-delete/<pk>/', projectperformancereview_delete, name='projectperformancereview_delete'),

    path('projectschedule/', projectschedule_create, name='projectschedule'),
    path('projectschedule-view/<pk>/', projectschedule_view, name='projectschedule_view'),
    path('projectschedule-edit/<pk>/', projectschedule_edit, name='projectschedule_edit'),
    path('projectschedule-delete/<pk>/', projectschedule_delete, name='projectschedule_delete'),

    path('punchlistitem/', punchlistitem_create, name='punchlistitem'),
    path('punchlistitem-view/<pk>/', punchlistitem_view, name='punchlistitem_view'),
    path('punchlistitem-edit/<pk>/', punchlistitem_edit, name='punchlistitem_edit'),
    path('punchlistitem-delete/<pk>/', punchlistitem_delete, name='punchlistitem_delete'),

    path('qualitycontrolplan/', qualitycontrolplan_create, name='qualitycontrolplan'),
    path('qualitycontrolplan-view/<pk>/', qualitycontrolplan_view, name='qualitycontrolplan_view'),
    path('qualitycontrolplan-edit/<pk>/', qualitycontrolplan_edit, name='qualitycontrolplan_edit'),
    path('qualitycontrolplan-delete/<pk>/', qualitycontrolplan_delete, name='qualitycontrolplan_delete'),

    path('qualityinspector/', qualityinspector_create, name='qualityinspector'),
    path('qualityinspector-view/<pk>/', qualityinspector_view, name='qualityinspector_view'),
    path('qualityinspector-edit/<pk>/', qualityinspector_edit, name='qualityinspector_edit'),
    path('qualityinspector-delete/<pk>/', qualityinspector_delete, name='qualityinspector_delete'),

    path('resourceplanning/', resourceplanning_create, name='resourceplanning'),
    path('resourceplanning-view/<pk>/', resourceplanning_view, name='resourceplanning_view'),
    path('resourceplanning-edit/<pk>/', resourceplanning_edit, name='resourceplanning_edit'),
    path('resourceplanning-delete/<pk>/', resourceplanning_delete, name='resourceplanning_delete'),

    path('resourceutilizationanalysis/', resourceutilizationanalysis_create, name='resourceutilizationanalysis'),
    path('resourceutilizationanalysis-view/<pk>/', resourceutilizationanalysis_view, name='resourceutilizationanalysis_view'),
    path('resourceutilizationanalysis-edit/<pk>/', resourceutilizationanalysis_edit, name='resourceutilizationanalysis_edit'),
    path('resourceutilizationanalysis-delete/<pk>/', resourceutilizationanalysis_delete, name='resourceutilizationanalysis_delete'),

    path('revenue/', revenue_create, name='revenue'),
    path('revenue-view/<pk>/', revenue_view, name='revenue_view'),
    path('revenue-edit/<pk>/', revenue_edit, name='revenue_edit'),
    path('revenue-delete/<pk>/', revenue_delete, name='revenue_delete'),

    path('risk/', risk_create, name='risk'),
    path('risk-view/<pk>/', risk_view, name='risk_view'),
    path('risk-edit/<pk>/', risk_edit, name='risk_edit'),
    path('risk-delete/<pk>/', risk_delete, name='risk_delete'),

    path('safetyofficer/', safetyofficer_create, name='safetyofficer'),
    path('safetyofficer-view/<pk>/', safetyofficer_view, name='safetyofficer_view'),
    path('safetyofficer-edit/<pk>/', safetyofficer_edit, name='safetyofficer_edit'),
    path('safetyofficer-delete/<pk>/', safetyofficer_delete, name='safetyofficer_delete'),

    path('safetyplan/', safetyplan_create, name='safetyplan'),
    path('safetyplan-view/<pk>/', safetyplan_view, name='safetyplan_view'),
    path('safetyplan-edit/<pk>/', safetyplan_edit, name='safetyplan_edit'),
    path('safetyplan-delete/<pk>/', safetyplan_delete, name='safetyplan_delete'),

    path('subcontractorcontract/', subcontractorcontract_create, name='subcontractorcontract'),
    path('subcontractorcontract-view/<pk>/', subcontractorcontract_view, name='subcontractorcontract_view'),
    path('subcontractorcontract-edit/<pk>/', subcontractorcontract_edit, name='subcontractorcontract_edit'),
    path('subcontractorcontract-delete/<pk>/', subcontractorcontract_delete, name='subcontractorcontract_delete'),

    path('resourceavailability/', resourceavailability_create, name='resourceavailability'),
    path('resourceavailability-view/<pk>/', resourceavailability_view, name='resourceavailability_view'),
    path('resourceavailability-edit/<pk>/', resourceavailability_edit, name='resourceavailability_edit'),
    path('resourceavailability-delete/<pk>/', resourceavailability_delete, name='resourceavailability_delete'),

    path('clarificationdocument/', clarificationdocument_create, name='clarificationdocument'),
    path('clarificationdocument-view/<pk>/', clarificationdocument_view, name='clarificationdocument_view'),
    path('clarificationdocument-edit/<pk>/', clarificationdocument_edit, name='clarificationdocument_edit'),
    path('clarificationdocument-delete/<pk>/', clarificationdocument_delete, name='clarificationdocument_delete'),

    path('stakeholder/', stakeholder_create, name='stakeholder'),
    path('stakeholder-view/<pk>/', stakeholder_view, name='stakeholder_view'),
    path('stakeholder-edit/<pk>/', stakeholder_edit, name='stakeholder_edit'),
    path('stakeholder-delete/<pk>/', stakeholder_delete, name='stakeholder_delete'),

    path('teammember/', teammember_create, name='teammember'),
    path('teammember-view/<pk>/', teammember_view, name='teammember_view'),
    path('teammember-edit/<pk>/', teammember_edit, name='teammember_edit'),
    path('teammember-delete/<pk>/', teammember_delete, name='teammember_delete'),

    path('expense/', expense_create, name='expense'),
    path('expense-view/<pk>/', expense_view, name='expense_view'),
    path('expense-edit/<pk>/', expense_edit, name='expense_edit'),
    path('expense-delete/<pk>/', expense_delete, name='expense_delete'),

    path('prequalificationquestionnaire/', prequalificationquestionnaire_create, name='prequalificationquestionnaire'),
    path('prequalificationquestionnaire-view/<pk>/', prequalificationquestionnaire_view, name='prequalificationquestionnaire_view'),
    path('prequalificationquestionnaire-edit/<pk>/', prequalificationquestionnaire_edit, name='prequalificationquestionnaire_edit'),
    path('prequalificationquestionnaire-delete/<pk>/', prequalificationquestionnaire_delete, name='prequalificationquestionnaire_delete'),

    path('rfprfqdistribution/', rfprfqdistribution_create, name='rfprfqdistribution'),
    path('rfprfqdistribution-view/<pk>/', rfprfqdistribution_view, name='rfprfqdistribution_view'),
    path('rfprfqdistribution-edit/<pk>/', rfprfqdistribution_edit, name='rfprfqdistribution_edit'),
    path('rfprfqdistribution-delete/<pk>/', rfprfqdistribution_delete, name='rfprfqdistribution_delete'),

    path('supplierperformanceevaluation/', supplierperformanceevaluation_create, name='supplierperformanceevaluation'),
    path('supplierperformanceevaluation-view/<pk>/', supplierperformanceevaluation_view, name='supplierperformanceevaluation_view'),
    path('supplierperformanceevaluation-edit/<pk>/', supplierperformanceevaluation_edit, name='supplierperformanceevaluation_edit'),
    path('supplierperformanceevaluation-delete/<pk>/', supplierperformanceevaluation_delete, name='supplierperformanceevaluation_delete'),

    path('vendorclarification/', vendorclarification_create, name='vendorclarification'),
    path('vendorclarification-view/<pk>/', vendorclarification_view, name='vendorclarification_view'),
    path('vendorclarification-edit/<pk>/', vendorclarification_edit, name='vendorclarification_edit'),
    path('vendorclarification-delete/<pk>/', vendorclarification_delete, name='vendorclarification_delete'),

    path('vendorprequalificationstatus/', vendorprequalificationstatus_create, name='vendorprequalificationstatus'),
    path('vendorprequalificationstatus-view/<pk>/', vendorprequalificationstatus_view, name='vendorprequalificationstatus_view'),
    path('vendorprequalificationstatus-edit/<pk>/', vendorprequalificationstatus_edit, name='vendorprequalificationstatus_edit'),
    path('vendorprequalificationstatus-delete/<pk>/', vendorprequalificationstatus_delete, name='vendorprequalificationstatus_delete'),

    path('vendorproposal/', vendorproposal_create, name='vendorproposal'),
    path('vendorproposal-view/<pk>/', vendorproposal_view, name='vendorproposal_view'),
    path('vendorproposal-edit/<pk>/', vendorproposal_edit, name='vendorproposal_edit'),
    path('vendorproposal-delete/<pk>/', vendorproposal_delete, name='vendorproposal_delete'),

    path('assetaudit/', assetaudit_create, name='assetaudit'),
    path('assetaudit-view/<pk>/', assetaudit_view, name='assetaudit_view'),
    path('assetaudit-edit/<pk>/', assetaudit_edit, name='assetaudit_edit'),
    path('assetaudit-delete/<pk>/', assetaudit_delete, name='assetaudit_delete'),

    path('assetmaintenance/', assetmaintenance_create, name='assetmaintenance'),
    path('assetmaintenance-view/<pk>/', assetmaintenance_view, name='assetmaintenance_view'),
    path('assetmaintenance-edit/<pk>/', assetmaintenance_edit, name='assetmaintenance_edit'),
    path('assetmaintenance-delete/<pk>/', assetmaintenance_delete, name='assetmaintenance_delete'),

    path('depreciation/', depreciation_create, name='depreciation'),
    path('depreciation-view/<pk>/', depreciation_view, name='depreciation_view'),
    path('depreciation-edit/<pk>/', depreciation_edit, name='depreciation_edit'),
    path('depreciation-delete/<pk>/', depreciation_delete, name='depreciation_delete'),

    path('submissionfollowup/', submissionfollowup_create, name='submissionfollowup'),
    path('submissionfollowup-view/<pk>/', submissionfollowup_view, name='submissionfollowup_view'),
    path('submissionfollowup-edit/<pk>/', submissionfollowup_edit, name='submissionfollowup_edit'),
    path('submissionfollowup-delete/<pk>/', submissionfollowup_delete, name='submissionfollowup_delete'),

    path('negotiationandaward/', negotiationandaward_create, name='negotiationandaward'),
    path('negotiationandaward-view/<pk>/', negotiationandaward_view, name='negotiationandaward_view'),
    path('negotiationandaward-edit/<pk>/', negotiationandaward_edit, name='negotiationandaward_edit'),
    path('negotiationandaward-delete/<pk>/', negotiationandaward_delete, name='negotiationandaward_delete'),

    path('postsubmissionfollowup/', postsubmissionfollowup_create, name='postsubmissionfollowup'),
    path('postsubmissionfollowup-view/<pk>/', postsubmissionfollowup_view, name='postsubmissionfollowup_view'),
    path('postsubmissionfollowup-edit/<pk>/', postsubmissionfollowup_edit, name='postsubmissionfollowup_edit'),
    path('postsubmissionfollowup-delete/<pk>/', postsubmissionfollowup_delete, name='postsubmissionfollowup_delete'),

    path('equipmentassignment/', equipmentassignment_create, name='equipmentassignment'),
    path('equipmentassignment-view/<pk>/', equipmentassignment_view, name='equipmentassignment_view'),
    path('equipmentassignment-edit/<pk>/', equipmentassignment_edit, name='equipmentassignment_edit'),
    path('equipmentassignment-delete/<pk>/', equipmentassignment_delete, name='equipmentassignment_delete'),

    path('equipmentaudit/', equipmentaudit_create, name='equipmentaudit'),
    path('equipmentaudit-view/<pk>/', equipmentaudit_view, name='equipmentaudit_view'),
    path('equipmentaudit-edit/<pk>/', equipmentaudit_edit, name='equipmentaudit_edit'),
    path('equipmentaudit-delete/<pk>/', equipmentaudit_delete, name='equipmentaudit_delete'),

    path('equipmentmaintenance/', equipmentmaintenance_create, name='equipmentmaintenance'),
    path('equipmentmaintenance-view/<pk>/', equipmentmaintenance_view, name='equipmentmaintenance_view'),
    path('equipmentmaintenance-edit/<pk>/', equipmentmaintenance_edit, name='equipmentmaintenance_edit'),
    path('equipmentmaintenance-delete/<pk>/', equipmentmaintenance_delete, name='equipmentmaintenance_delete'),

    path('inventoryaudit/', inventoryaudit_create, name='inventoryaudit'),
    path('inventoryaudit-view/<pk>/', inventoryaudit_view, name='inventoryaudit_view'),
    path('inventoryaudit-edit/<pk>/', inventoryaudit_edit, name='inventoryaudit_edit'),
    path('inventoryaudit-delete/<pk>/', inventoryaudit_delete, name='inventoryaudit_delete'),

    path('requisition/', requisition_create, name='requisition'),
    path('requisition-view/<pk>/', requisition_view, name='requisition_view'),
    path('requisition-edit/<pk>/', requisition_edit, name='requisition_edit'),
    path('requisition-delete/<pk>/', requisition_delete, name='requisition_delete'),

    path('stockentry/', stockentry_create, name='stockentry'),
    path('stockentry-view/<pk>/', stockentry_view, name='stockentry_view'),
    path('stockentry-edit/<pk>/', stockentry_edit, name='stockentry_edit'),
    path('stockentry-delete/<pk>/', stockentry_delete, name='stockentry_delete'),

    path('clientinteraction/', clientinteraction_create, name='clientinteraction'),
    path('clientinteraction-view/<pk>/', clientinteraction_view, name='clientinteraction_view'),
    path('clientinteraction-edit/<pk>/', clientinteraction_edit, name='clientinteraction_edit'),
    path('clientinteraction-delete/<pk>/', clientinteraction_delete, name='clientinteraction_delete'),

    path('opportunity/', opportunity_create, name='opportunity'),
    path('opportunity-view/<pk>/', opportunity_view, name='opportunity_view'),
    path('opportunity-edit/<pk>/', opportunity_edit, name='opportunity_edit'),
    path('opportunity-delete/<pk>/', opportunity_delete, name='opportunity_delete'),

    path('documentedrequirement/', documentedrequirement_create, name='documentedrequirement'),
    path('documentedrequirement-view/<pk>/', documentedrequirement_view, name='documentedrequirement_view'),
    path('documentedrequirement-edit/<pk>/', documentedrequirement_edit, name='documentedrequirement_edit'),
    path('documentedrequirement-delete/<pk>/', documentedrequirement_delete, name='documentedrequirement_delete'),

    path('correctivepreventiveaction/', correctivepreventiveaction_create, name='correctivepreventiveaction'),
    path('correctivepreventiveaction-view/<pk>/', correctivepreventiveaction_view, name='correctivepreventiveaction_view'),
    path('correctivepreventiveaction-edit/<pk>/', correctivepreventiveaction_edit, name='correctivepreventiveaction_edit'),
    path('correctivepreventiveaction-delete/<pk>/', correctivepreventiveaction_delete, name='correctivepreventiveaction_delete'),

    path('changeorder/', changeorder_create, name='changeorder'),
    path('changeorder-view/<pk>/', changeorder_view, name='changeorder_view'),
    path('changeorder-edit/<pk>/', changeorder_edit, name='changeorder_edit'),
    path('changeorder-delete/<pk>/', changeorder_delete, name='changeorder_delete'),

    path('contractcloseout/', contractcloseout_create, name='contractcloseout'),
    path('contractcloseout-view/<pk>/', contractcloseout_view, name='contractcloseout_view'),
    path('contractcloseout-edit/<pk>/', contractcloseout_edit, name='contractcloseout_edit'),
    path('contractcloseout-delete/<pk>/', contractcloseout_delete, name='contractcloseout_delete'),

    path('contractexecution/', contractexecution_create, name='contractexecution'),
    path('contractexecution-view/<pk>/', contractexecution_view, name='contractexecution_view'),
    path('contractexecution-edit/<pk>/', contractexecution_edit, name='contractexecution_edit'),
    path('contractexecution-delete/<pk>/', contractexecution_delete, name='contractexecution_delete'),

    path('contractmilestone/', contractmilestone_create, name='contractmilestone'),
    path('contractmilestone-view/<pk>/', contractmilestone_view, name='contractmilestone_view'),
    path('contractmilestone-edit/<pk>/', contractmilestone_edit, name='contractmilestone_edit'),
    path('contractmilestone-delete/<pk>/', contractmilestone_delete, name='contractmilestone_delete'),

    path('legalreview/', legalreview_create, name='legalreview'),
    path('legalreview-view/<pk>/', legalreview_view, name='legalreview_view'),
    path('legalreview-edit/<pk>/', legalreview_edit, name='legalreview_edit'),
    path('legalreview-delete/<pk>/', legalreview_delete, name='legalreview_delete'),

    path('purchaseorder/', purchaseorder_create, name='purchaseorder'),
    path('purchaseorder-view/<pk>/', purchaseorder_view, name='purchaseorder_view'),
    path('purchaseorder-edit/<pk>/', purchaseorder_edit, name='purchaseorder_edit'),
    path('purchaseorder-delete/<pk>/', purchaseorder_delete, name='purchaseorder_delete'),

    path('correctiveaction/', correctiveaction_create, name='correctiveaction'),
    path('correctiveaction-view/<pk>/', correctiveaction_view, name='correctiveaction_view'),
    path('correctiveaction-edit/<pk>/', correctiveaction_edit, name='correctiveaction_edit'),
    path('correctiveaction-delete/<pk>/', correctiveaction_delete, name='correctiveaction_delete'),

    path('investigation/', investigation_create, name='investigation'),
    path('investigation-view/<pk>/', investigation_view, name='investigation_view'),
    path('investigation-edit/<pk>/', investigation_edit, name='investigation_edit'),
    path('investigation-delete/<pk>/', investigation_delete, name='investigation_delete'),

    path('clientreview/', clientreview_create, name='clientreview'),
    path('clientreview-view/<pk>/', clientreview_view, name='clientreview_view'),
    path('clientreview-edit/<pk>/', clientreview_edit, name='clientreview_edit'),
    path('clientreview-delete/<pk>/', clientreview_delete, name='clientreview_delete'),

    path('scheduleadjustment/', scheduleadjustment_create, name='scheduleadjustment'),
    path('scheduleadjustment-view/<pk>/', scheduleadjustment_view, name='scheduleadjustment_view'),
    path('scheduleadjustment-edit/<pk>/', scheduleadjustment_edit, name='scheduleadjustment_edit'),
    path('scheduleadjustment-delete/<pk>/', scheduleadjustment_delete, name='scheduleadjustment_delete'),

    path('task/', task_create, name='task'),
    path('task-view/<pk>/', task_view, name='task_view'),
    path('task-edit/<pk>/', task_edit, name='task_edit'),
    path('task-delete/<pk>/', task_delete, name='task_delete'),

    path('siteinspection/', siteinspection_create, name='siteinspection'),
    path('siteinspection-view/<pk>/', siteinspection_view, name='siteinspection_view'),
    path('siteinspection-edit/<pk>/', siteinspection_edit, name='siteinspection_edit'),
    path('siteinspection-delete/<pk>/', siteinspection_delete, name='siteinspection_delete'),

    path('machinery/', machinery_create, name='machinery'),
    path('machinery-view/<pk>/', machinery_view, name='machinery_view'),
    path('machinery-edit/<pk>/', machinery_edit, name='machinery_edit'),
    path('machinery-delete/<pk>/', machinery_delete, name='machinery_delete'),

    path('material/', material_create, name='material'),
    path('material-view/<pk>/', material_view, name='material_view'),
    path('material-edit/<pk>/', material_edit, name='material_edit'),
    path('material-delete/<pk>/', material_delete, name='material_delete'),

    path('mitigationstrategy/', mitigationstrategy_create, name='mitigationstrategy'),
    path('mitigationstrategy-view/<pk>/', mitigationstrategy_view, name='mitigationstrategy_view'),
    path('mitigationstrategy-edit/<pk>/', mitigationstrategy_edit, name='mitigationstrategy_edit'),
    path('mitigationstrategy-delete/<pk>/', mitigationstrategy_delete, name='mitigationstrategy_delete'),

    path('riskassessment/', riskassessment_create, name='riskassessment'),
    path('riskassessment-view/<pk>/', riskassessment_view, name='riskassessment_view'),
    path('riskassessment-edit/<pk>/', riskassessment_edit, name='riskassessment_edit'),
    path('riskassessment-delete/<pk>/', riskassessment_delete, name='riskassessment_delete'),

    path('riskreview/', riskreview_create, name='riskreview'),
    path('riskreview-view/<pk>/', riskreview_view, name='riskreview_view'),
    path('riskreview-edit/<pk>/', riskreview_edit, name='riskreview_edit'),
    path('riskreview-delete/<pk>/', riskreview_delete, name='riskreview_delete'),

    path('delaynotification/', delaynotification_create, name='delaynotification'),
    path('delaynotification-view/<pk>/', delaynotification_view, name='delaynotification_view'),
    path('delaynotification-edit/<pk>/', delaynotification_edit, name='delaynotification_edit'),
    path('delaynotification-delete/<pk>/', delaynotification_delete, name='delaynotification_delete'),

    path('stakeholderinput/', stakeholderinput_create, name='stakeholderinput'),
    path('stakeholderinput-view/<pk>/', stakeholderinput_view, name='stakeholderinput_view'),
    path('stakeholderinput-edit/<pk>/', stakeholderinput_edit, name='stakeholderinput_edit'),
    path('stakeholderinput-delete/<pk>/', stakeholderinput_delete, name='stakeholderinput_delete'),

    path('tenderdocument/', tenderdocument_create, name='tenderdocument'),
    path('tenderdocument-view/<pk>/', tenderdocument_view, name='tenderdocument_view'),
    path('tenderdocument-edit/<pk>/', tenderdocument_edit, name='tenderdocument_edit'),
    path('tenderdocument-delete/<pk>/', tenderdocument_delete, name='tenderdocument_delete'),

    path('issue/', issue_create, name='issue'),
    path('issue-view/<pk>/', issue_view, name='issue_view'),
    path('issue-edit/<pk>/', issue_edit, name='issue_edit'),
    path('issue-delete/<pk>/', issue_delete, name='issue_delete'),

    path('rfprfqresponse/', rfprfqresponse_create, name='rfprfqresponse'),
    path('rfprfqresponse-view/<pk>/', rfprfqresponse_view, name='rfprfqresponse_view'),
    path('rfprfqresponse-edit/<pk>/', rfprfqresponse_edit, name='rfprfqresponse_edit'),
    path('rfprfqresponse-delete/<pk>/', rfprfqresponse_delete, name='rfprfqresponse_delete'),

    path('clarificationresponse/', clarificationresponse_create, name='clarificationresponse'),
    path('clarificationresponse-view/<pk>/', clarificationresponse_view, name='clarificationresponse_view'),
    path('clarificationresponse-edit/<pk>/', clarificationresponse_edit, name='clarificationresponse_edit'),
    path('clarificationresponse-delete/<pk>/', clarificationresponse_delete, name='clarificationresponse_delete'),

    path('finalvendorselection/', finalvendorselection_create, name='finalvendorselection'),
    path('finalvendorselection-view/<pk>/', finalvendorselection_view, name='finalvendorselection_view'),
    path('finalvendorselection-edit/<pk>/', finalvendorselection_edit, name='finalvendorselection_edit'),
    path('finalvendorselection-delete/<pk>/', finalvendorselection_delete, name='finalvendorselection_delete'),

    path('financialevaluation/', financialevaluation_create, name='financialevaluation'),
    path('financialevaluation-view/<pk>/', financialevaluation_view, name='financialevaluation_view'),
    path('financialevaluation-edit/<pk>/', financialevaluation_edit, name='financialevaluation_edit'),
    path('financialevaluation-delete/<pk>/', financialevaluation_delete, name='financialevaluation_delete'),

    path('negotiationstakeholder/', negotiationstakeholder_create, name='negotiationstakeholder'),
    path('negotiationstakeholder-view/<pk>/', negotiationstakeholder_view, name='negotiationstakeholder_view'),
    path('negotiationstakeholder-edit/<pk>/', negotiationstakeholder_edit, name='negotiationstakeholder_edit'),
    path('negotiationstakeholder-delete/<pk>/', negotiationstakeholder_delete, name='negotiationstakeholder_delete'),

    path('negotiationsummary/', negotiationsummary_create, name='negotiationsummary'),
    path('negotiationsummary-view/<pk>/', negotiationsummary_view, name='negotiationsummary_view'),
    path('negotiationsummary-edit/<pk>/', negotiationsummary_edit, name='negotiationsummary_edit'),
    path('negotiationsummary-delete/<pk>/', negotiationsummary_delete, name='negotiationsummary_delete'),

    path('negotiationterm/', negotiationterm_create, name='negotiationterm'),
    path('negotiationterm-view/<pk>/', negotiationterm_view, name='negotiationterm_view'),
    path('negotiationterm-edit/<pk>/', negotiationterm_edit, name='negotiationterm_edit'),
    path('negotiationterm-delete/<pk>/', negotiationterm_delete, name='negotiationterm_delete'),

    path('proposalcompliance/', proposalcompliance_create, name='proposalcompliance'),
    path('proposalcompliance-view/<pk>/', proposalcompliance_view, name='proposalcompliance_view'),
    path('proposalcompliance-edit/<pk>/', proposalcompliance_edit, name='proposalcompliance_edit'),
    path('proposalcompliance-delete/<pk>/', proposalcompliance_delete, name='proposalcompliance_delete'),

    path('proposalevaluation/', proposalevaluation_create, name='proposalevaluation'),
    path('proposalevaluation-view/<pk>/', proposalevaluation_view, name='proposalevaluation_view'),
    path('proposalevaluation-edit/<pk>/', proposalevaluation_edit, name='proposalevaluation_edit'),
    path('proposalevaluation-delete/<pk>/', proposalevaluation_delete, name='proposalevaluation_delete'),

    path('proposalscoring/', proposalscoring_create, name='proposalscoring'),
    path('proposalscoring-view/<pk>/', proposalscoring_view, name='proposalscoring_view'),
    path('proposalscoring-edit/<pk>/', proposalscoring_edit, name='proposalscoring_edit'),
    path('proposalscoring-delete/<pk>/', proposalscoring_delete, name='proposalscoring_delete'),

    path('riskevaluation/', riskevaluation_create, name='riskevaluation'),
    path('riskevaluation-view/<pk>/', riskevaluation_view, name='riskevaluation_view'),
    path('riskevaluation-edit/<pk>/', riskevaluation_edit, name='riskevaluation_edit'),
    path('riskevaluation-delete/<pk>/', riskevaluation_delete, name='riskevaluation_delete'),

    path('technicalevaluation/', technicalevaluation_create, name='technicalevaluation'),
    path('technicalevaluation-view/<pk>/', technicalevaluation_view, name='technicalevaluation_view'),
    path('technicalevaluation-edit/<pk>/', technicalevaluation_edit, name='technicalevaluation_edit'),
    path('technicalevaluation-delete/<pk>/', technicalevaluation_delete, name='technicalevaluation_delete'),

    path('proposal/', proposal_create, name='proposal'),
    path('proposal-view/<pk>/', proposal_view, name='proposal_view'),
    path('proposal-edit/<pk>/', proposal_edit, name='proposal_edit'),
    path('proposal-delete/<pk>/', proposal_delete, name='proposal_delete'),

    path('auditlog/', auditlog_create, name='auditlog'),
    path('auditlog-view/<pk>/', auditlog_view, name='auditlog_view'),
    path('auditlog-edit/<pk>/', auditlog_edit, name='auditlog_edit'),
    path('auditlog-delete/<pk>/', auditlog_delete, name='auditlog_delete'),

    path('changeorderapproval/', changeorderapproval_create, name='changeorderapproval'),
    path('changeorderapproval-view/<pk>/', changeorderapproval_view, name='changeorderapproval_view'),
    path('changeorderapproval-edit/<pk>/', changeorderapproval_edit, name='changeorderapproval_edit'),
    path('changeorderapproval-delete/<pk>/', changeorderapproval_delete, name='changeorderapproval_delete'),

    path('changeorderimplementation/', changeorderimplementation_create, name='changeorderimplementation'),
    path('changeorderimplementation-view/<pk>/', changeorderimplementation_view, name='changeorderimplementation_view'),
    path('changeorderimplementation-edit/<pk>/', changeorderimplementation_edit, name='changeorderimplementation_edit'),
    path('changeorderimplementation-delete/<pk>/', changeorderimplementation_delete, name='changeorderimplementation_delete'),

    path('document/', document_create, name='document'),
    path('document-view/<pk>/', document_view, name='document_view'),
    path('document-edit/<pk>/', document_edit, name='document_edit'),
    path('document-delete/<pk>/', document_delete, name='document_delete'),

    path('invoice/', invoice_create, name='invoice'),
    path('invoice-view/<pk>/', invoice_view, name='invoice_view'),
    path('invoice-edit/<pk>/', invoice_edit, name='invoice_edit'),
    path('invoice-delete/<pk>/', invoice_delete, name='invoice_delete'),

    path('shipment/', shipment_create, name='shipment'),
    path('shipment-view/<pk>/', shipment_view, name='shipment_view'),
    path('shipment-edit/<pk>/', shipment_edit, name='shipment_edit'),
    path('shipment-delete/<pk>/', shipment_delete, name='shipment_delete'),

    path('criticalpath/', criticalpath_create, name='criticalpath'),
    path('criticalpath-view/<pk>/', criticalpath_view, name='criticalpath_view'),
    path('criticalpath-edit/<pk>/', criticalpath_edit, name='criticalpath_edit'),
    path('criticalpath-delete/<pk>/', criticalpath_delete, name='criticalpath_delete'),

    path('dailyprogressreport/', dailyprogressreport_create, name='dailyprogressreport'),
    path('dailyprogressreport-view/<pk>/', dailyprogressreport_view, name='dailyprogressreport_view'),
    path('dailyprogressreport-edit/<pk>/', dailyprogressreport_edit, name='dailyprogressreport_edit'),
    path('dailyprogressreport-delete/<pk>/', dailyprogressreport_delete, name='dailyprogressreport_delete'),

    path('delay/', delay_create, name='delay'),
    path('delay-view/<pk>/', delay_view, name='delay_view'),
    path('delay-edit/<pk>/', delay_edit, name='delay_edit'),
    path('delay-delete/<pk>/', delay_delete, name='delay_delete'),

    path('performancereport/', performancereport_create, name='performancereport'),
    path('performancereport-view/<pk>/', performancereport_view, name='performancereport_view'),
    path('performancereport-edit/<pk>/', performancereport_edit, name='performancereport_edit'),
    path('performancereport-delete/<pk>/', performancereport_delete, name='performancereport_delete'),

    path('photodocumentation/', photodocumentation_create, name='photodocumentation'),
    path('photodocumentation-view/<pk>/', photodocumentation_view, name='photodocumentation_view'),
    path('photodocumentation-edit/<pk>/', photodocumentation_edit, name='photodocumentation_edit'),
    path('photodocumentation-delete/<pk>/', photodocumentation_delete, name='photodocumentation_delete'),

    path('projectupdate/', projectupdate_create, name='projectupdate'),
    path('projectupdate-view/<pk>/', projectupdate_view, name='projectupdate_view'),
    path('projectupdate-edit/<pk>/', projectupdate_edit, name='projectupdate_edit'),
    path('projectupdate-delete/<pk>/', projectupdate_delete, name='projectupdate_delete'),

    path('resourceadjustment/', resourceadjustment_create, name='resourceadjustment'),
    path('resourceadjustment-view/<pk>/', resourceadjustment_view, name='resourceadjustment_view'),
    path('resourceadjustment-edit/<pk>/', resourceadjustment_edit, name='resourceadjustment_edit'),
    path('resourceadjustment-delete/<pk>/', resourceadjustment_delete, name='resourceadjustment_delete'),

    path('resourceallocation/', resourceallocation_create, name='resourceallocation'),
    path('resourceallocation-view/<pk>/', resourceallocation_view, name='resourceallocation_view'),
    path('resourceallocation-edit/<pk>/', resourceallocation_edit, name='resourceallocation_edit'),
    path('resourceallocation-delete/<pk>/', resourceallocation_delete, name='resourceallocation_delete'),

    path('taskdependency/', taskdependency_create, name='taskdependency'),
    path('taskdependency-view/<pk>/', taskdependency_view, name='taskdependency_view'),
    path('taskdependency-edit/<pk>/', taskdependency_edit, name='taskdependency_edit'),
    path('taskdependency-delete/<pk>/', taskdependency_delete, name='taskdependency_delete'),

    path('taskresourceallocation/', taskresourceallocation_create, name='taskresourceallocation'),
    path('taskresourceallocation-view/<pk>/', taskresourceallocation_view, name='taskresourceallocation_view'),
    path('taskresourceallocation-edit/<pk>/', taskresourceallocation_edit, name='taskresourceallocation_edit'),
    path('taskresourceallocation-delete/<pk>/', taskresourceallocation_delete, name='taskresourceallocation_delete'),

    path('taskschedule/', taskschedule_create, name='taskschedule'),
    path('taskschedule-view/<pk>/', taskschedule_view, name='taskschedule_view'),
    path('taskschedule-edit/<pk>/', taskschedule_edit, name='taskschedule_edit'),
    path('taskschedule-delete/<pk>/', taskschedule_delete, name='taskschedule_delete'),

    path('taskstatus/', taskstatus_create, name='taskstatus'),
    path('taskstatus-view/<pk>/', taskstatus_view, name='taskstatus_view'),
    path('taskstatus-edit/<pk>/', taskstatus_edit, name='taskstatus_edit'),
    path('taskstatus-delete/<pk>/', taskstatus_delete, name='taskstatus_delete'),

    path('timesheet/', timesheet_create, name='timesheet'),
    path('timesheet-view/<pk>/', timesheet_view, name='timesheet_view'),
    path('timesheet-edit/<pk>/', timesheet_edit, name='timesheet_edit'),
    path('timesheet-delete/<pk>/', timesheet_delete, name='timesheet_delete'),

    path('timetracking/', timetracking_create, name='timetracking'),
    path('timetracking-view/<pk>/', timetracking_view, name='timetracking_view'),
    path('timetracking-edit/<pk>/', timetracking_edit, name='timetracking_edit'),
    path('timetracking-delete/<pk>/', timetracking_delete, name='timetracking_delete'),

    path('stockadjustment/', stockadjustment_create, name='stockadjustment'),
    path('stockadjustment-view/<pk>/', stockadjustment_view, name='stockadjustment_view'),
    path('stockadjustment-edit/<pk>/', stockadjustment_edit, name='stockadjustment_edit'),
    path('stockadjustment-delete/<pk>/', stockadjustment_delete, name='stockadjustment_delete'),

    path('stockreplenishmentrequest/', stockreplenishmentrequest_create, name='stockreplenishmentrequest'),
    path('stockreplenishmentrequest-view/<pk>/', stockreplenishmentrequest_view, name='stockreplenishmentrequest_view'),
    path('stockreplenishmentrequest-edit/<pk>/', stockreplenishmentrequest_edit, name='stockreplenishmentrequest_edit'),
    path('stockreplenishmentrequest-delete/<pk>/', stockreplenishmentrequest_delete, name='stockreplenishmentrequest_delete'),

    path('mitigationaction/', mitigationaction_create, name='mitigationaction'),
    path('mitigationaction-view/<pk>/', mitigationaction_view, name='mitigationaction_view'),
    path('mitigationaction-edit/<pk>/', mitigationaction_edit, name='mitigationaction_edit'),
    path('mitigationaction-delete/<pk>/', mitigationaction_delete, name='mitigationaction_delete'),

    path('tenderscope/', tenderscope_create, name='tenderscope'),
    path('tenderscope-view/<pk>/', tenderscope_view, name='tenderscope_view'),
    path('tenderscope-edit/<pk>/', tenderscope_edit, name='tenderscope_edit'),
    path('tenderscope-delete/<pk>/', tenderscope_delete, name='tenderscope_delete'),

    path('tendersubmission/', tendersubmission_create, name='tendersubmission'),
    path('tendersubmission-view/<pk>/', tendersubmission_view, name='tendersubmission_view'),
    path('tendersubmission-edit/<pk>/', tendersubmission_edit, name='tendersubmission_edit'),
    path('tendersubmission-delete/<pk>/', tendersubmission_delete, name='tendersubmission_delete'),

    path('contractaward/', contractaward_create, name='contractaward'),
    path('contractaward-view/<pk>/', contractaward_view, name='contractaward_view'),
    path('contractaward-edit/<pk>/', contractaward_edit, name='contractaward_edit'),
    path('contractaward-delete/<pk>/', contractaward_delete, name='contractaward_delete'),

    path('stakeholderevaluation/', stakeholderevaluation_create, name='stakeholderevaluation'),
    path('stakeholderevaluation-view/<pk>/', stakeholderevaluation_view, name='stakeholderevaluation_view'),
    path('stakeholderevaluation-edit/<pk>/', stakeholderevaluation_edit, name='stakeholderevaluation_edit'),
    path('stakeholderevaluation-delete/<pk>/', stakeholderevaluation_delete, name='stakeholderevaluation_delete'),

    path('payment/', payment_create, name='payment'),
    path('payment-view/<pk>/', payment_view, name='payment_view'),
    path('payment-edit/<pk>/', payment_edit, name='payment_edit'),
    path('payment-delete/<pk>/', payment_delete, name='payment_delete'),

    path('criticalpathmonitoring/', criticalpathmonitoring_create, name='criticalpathmonitoring'),
    path('criticalpathmonitoring-view/<pk>/', criticalpathmonitoring_view, name='criticalpathmonitoring_view'),
    path('criticalpathmonitoring-edit/<pk>/', criticalpathmonitoring_edit, name='criticalpathmonitoring_edit'),
    path('criticalpathmonitoring-delete/<pk>/', criticalpathmonitoring_delete, name='criticalpathmonitoring_delete'),

    path('adjustment/', adjustment_create, name='adjustment'),
    path('adjustment-view/<pk>/', adjustment_view, name='adjustment_view'),
    path('adjustment-edit/<pk>/', adjustment_edit, name='adjustment_edit'),
    path('adjustment-delete/<pk>/', adjustment_delete, name='adjustment_delete'),

    path('resourcereallocation/', resourcereallocation_create, name='resourcereallocation'),
    path('resourcereallocation-view/<pk>/', resourcereallocation_view, name='resourcereallocation_view'),
    path('resourcereallocation-edit/<pk>/', resourcereallocation_edit, name='resourcereallocation_edit'),
    path('resourcereallocation-delete/<pk>/', resourcereallocation_delete, name='resourcereallocation_delete'),

    path('resourceusage/', resourceusage_create, name='resourceusage'),
    path('resourceusage-view/<pk>/', resourceusage_view, name='resourceusage_view'),
    path('resourceusage-edit/<pk>/', resourceusage_edit, name='resourceusage_edit'),
    path('resourceusage-delete/<pk>/', resourceusage_delete, name='resourceusage_delete'),

    path('client/', client_create, name='client'),
    path('client-view/<pk>/', client_view, name='client_view'),
    path('client-edit/<pk>/', client_edit, name='client_edit'),
    path('client-delete/<pk>/', client_delete, name='client_delete'),

    path('bidqualification/', bidqualification_create, name='bidqualification'),
    path('bidqualification-view/<pk>/', bidqualification_view, name='bidqualification_view'),
    path('bidqualification-edit/<pk>/', bidqualification_edit, name='bidqualification_edit'),
    path('bidqualification-delete/<pk>/', bidqualification_delete, name='bidqualification_delete'),

    path('tenderproposalmanagement/', tenderproposalmanagement_create, name='tenderproposalmanagement'),
    path('tenderproposalmanagement-view/<pk>/', tenderproposalmanagement_view, name='tenderproposalmanagement_view'),
    path('tenderproposalmanagement-edit/<pk>/', tenderproposalmanagement_edit, name='tenderproposalmanagement_edit'),
    path('tenderproposalmanagement-delete/<pk>/', tenderproposalmanagement_delete, name='tenderproposalmanagement_delete'),
]

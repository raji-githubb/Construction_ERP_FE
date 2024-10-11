from django import forms 
class UserForm(forms.Form):
	first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	middle_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	dob = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	phone_number = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))

class AssetCategoryForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class WarehouseForm(forms.Form):
	location = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	capacity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))

class SubcontractorForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	address = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	certification = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	experience_years = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	financial_stability_rating = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	references = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	status = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	date_prequalified = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))

class OpportunityIdentificationForm(forms.Form):
	tender_title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	tender_type = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	identification_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	source = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	relevant_to_company = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))

class BidProposalForm(forms.Form):
	rfp_rfq_title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	technical_proposal = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	financial_proposal = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	internal_collaboration = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	submission_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	status = forms.ChoiceField(choices=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], required=True, widget=forms.Select(attrs={"class": "form-control"}))

class CurrencyForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	symbol = forms.CharField(max_length=5, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	exchange_rate = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))

class ClientInteractionTypeForm(forms.Form):
	type_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class CostCategoryForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))

class EquipmentCategoryForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class AccountForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	account_type = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	balance = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))

class ItemCategoryForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class SupplierForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	contact_person = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	address = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))

class LeadSourceForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))

class SalesRepresentativeForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class RiskOwnerForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class SalesStageForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class CustomerForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	contact_person = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	address = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))

class RiskCategoryForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))

class ContractorForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	contact_person = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	contact_phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class DelayCauseForm(forms.Form):
	cause = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class IndividualForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	skills = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))

class InternalDepartmentForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class ProjectForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	projected_end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	progress = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	budget = forms.FloatField( required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))
	location = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	manager_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		manager_list = kwargs.pop('manager_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['manager_id'].choices = [(item['id'], item['first_name']) for item in manager_list]

class ResourceForm(forms.Form):
	resource_type = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))

class RFPRFQForm(forms.Form):
	title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	document_type = forms.ChoiceField(choices=[('RFP', 'Rfp'), ('RFQ', 'Rfq')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	submission_deadline = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	procurement_manager = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class RoleForm(forms.Form):
	name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))

class ScoringCriteriaForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	weight = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))

class TaskCategoryForm(forms.Form):
	category_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class TaskPriorityForm(forms.Form):
	priority_level = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class TeamForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))

class VendorForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	contact_person = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	address = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	financial_standing = forms.FloatField( required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))
	financial_standing = forms.FloatField( required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))

class AssetForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	category_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	purchase_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	purchase_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	depreciation_rate = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	location_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	assigned_to = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('Active', 'Active'), ('Retired', 'Retired')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		category_list = kwargs.pop('category_choice', [])
		location_list = kwargs.pop('location_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['category_id'].choices = [(item['id'], item['name']) for item in category_list]
		self.fields['location_id'].choices = [(item['id'], item['location']) for item in location_list]

class ExpertiseForm(forms.Form):
	subcontractor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	area_of_expertise = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	certifications = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	performance_rating = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		subcontractor_list = kwargs.pop('subcontractor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['subcontractor_id'].choices = [(item['id'], item['name']) for item in subcontractor_list]

class BidNoBidDecisionForm(forms.Form):
	opportunity_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	decision_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	is_bid = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	rationale = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	profitability_assessment = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	resource_capacity_assessment = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		opportunity_list = kwargs.pop('opportunity_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['opportunity_id'].choices = [(item['id'], item['tender_title']) for item in opportunity_list]

class ProposalPreparationForm(forms.Form):
	opportunity_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	proposal_title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	technical_solutions = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	pricing = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	timelines = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	value_propositions = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	compliance_check = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		opportunity_list = kwargs.pop('opportunity_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['opportunity_id'].choices = [(item['id'], item['tender_title']) for item in opportunity_list]

class BidSubmissionForm(forms.Form):
	bid_proposal_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	submission_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	submission_method = forms.ChoiceField(choices=[('portal', 'Portal'), ('email', 'Email'), ('physical', 'Physical')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	documents_included = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		bid_proposal_list = kwargs.pop('bid_proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['bid_proposal_id'].choices = [(item['id'], item['rfp_rfq_title']) for item in bid_proposal_list]

class EquipmentForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	category_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	serial_number = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	purchase_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	condition = forms.ChoiceField(choices=[('New', 'New'), ('Used', 'Used')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	location_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('Available', 'Available'), ('In Use', 'In use'), ('Under Maintenance', 'Under maintenance')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		category_list = kwargs.pop('category_choice', [])
		location_list = kwargs.pop('location_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['category_id'].choices = [(item['id'], item['name']) for item in category_list]
		self.fields['location_id'].choices = [(item['id'], item['location']) for item in location_list]

class NotificationForm(forms.Form):
	message = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	is_read = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))

class ItemForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	category_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	supplier_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	stock_quantity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	reorder_point = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	safety_stock = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	price_per_unit = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	warehouse_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	barcode = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		category_list = kwargs.pop('category_choice', [])
		supplier_list = kwargs.pop('supplier_choice', [])
		warehouse_list = kwargs.pop('warehouse_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['category_id'].choices = [(item['id'], item['name']) for item in category_list]
		self.fields['supplier_id'].choices = [(item['id'], item['name']) for item in supplier_list]
		self.fields['warehouse_id'].choices = [(item['id'], item['location']) for item in warehouse_list]

class LeadForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	company = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	project_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	source_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('new', 'New'), ('qualified', 'Qualified'), ('disqualified', 'Disqualified')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	budget = forms.FloatField( required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))
	urgency = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	decision_maker = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	assigned_to_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		source_list = kwargs.pop('source_choice', [])
		assigned_to_list = kwargs.pop('assigned_to_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['source_id'].choices = [(item['id'], item['name']) for item in source_list]
		self.fields['assigned_to_id'].choices = [(item['id'], item['name']) for item in assigned_to_list]

class ProcurementNeedForm(forms.Form):
	department_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	date_needed = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		department_list = kwargs.pop('department_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['department_id'].choices = [(item['id'], item['name']) for item in department_list]

class AuditForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	audit_type = forms.ChoiceField(choices=[('Safety', 'Safety'), ('Quality', 'Quality')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	conducted_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	findings = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		conducted_by_list = kwargs.pop('conducted_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['conducted_by_id'].choices = [(item['id'], item['first_name']) for item in conducted_by_list]

class BidForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	subcontractor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	bid_amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	bid_submission_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	status = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		subcontractor_list = kwargs.pop('subcontractor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['subcontractor_id'].choices = [(item['id'], item['name']) for item in subcontractor_list]

class BudgetForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	total_budget = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	allocated_budget = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	remaining_budget = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	currency_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		currency_list = kwargs.pop('currency_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['currency_id'].choices = [(item['id'], item['name']) for item in currency_list]

class BudgetAllocationForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	materials_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	labor_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	equipment_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	contingency_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_budget = forms.FloatField( required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ClientFeedbackForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	feedback_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	client_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	satisfaction_rating = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ClientFollowUpForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	follow_up_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	message = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	action_taken = forms.ChoiceField(choices=[('email_sent', 'Email_sent'), ('called', 'Called')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ClientSatisfactionSurveyForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	sent_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	client_feedback = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	score = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class CloseoutDocumentForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	document_type = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ComplianceMonitorForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	compliance_type = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('Compliant', 'Compliant'), ('Non-compliant', 'Non-compliant')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ContractForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	contractor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	scope_of_work = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	pricing = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	payment_terms = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	signed_by_client = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	signed_by_contractor = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	approved_by = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	status = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		contractor_list = kwargs.pop('contractor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['contractor_id'].choices = [(item['id'], item['name']) for item in contractor_list]

class ContractAwardExecutionForm(forms.Form):
	contract_title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	project_manager_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	execution_status = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	delivery_commitments = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	execution_notes = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_manager_list = kwargs.pop('project_manager_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_manager_id'].choices = [(item['id'], item['name']) for item in project_manager_list]

class CostEstimationForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	category_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	estimated_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	actual_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	forecast_cost = forms.FloatField( required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		category_list = kwargs.pop('category_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['category_id'].choices = [(item['id'], item['name']) for item in category_list]

class FinalClientSignOffForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	client_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	sign_off_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	is_approved = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		client_list = kwargs.pop('client_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['client_id'].choices = [(item['id'], item['first_name']) for item in client_list]

class FinalInspectionForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	inspection_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	inspector_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	client_present = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	all_punch_items_resolved = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		inspector_list = kwargs.pop('inspector_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['inspector_id'].choices = [(item['id'], item['first_name']) for item in inspector_list]

class FinalReviewForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	review_type = forms.ChoiceField(choices=[('Safety', 'Safety'), ('Quality', 'Quality')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	review_details = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	conducted_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		conducted_by_list = kwargs.pop('conducted_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['conducted_by_id'].choices = [(item['id'], item['first_name']) for item in conducted_by_list]

class FinancialTransactionForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	account_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	transaction_type = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		account_list = kwargs.pop('account_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['account_id'].choices = [(item['id'], item['name']) for item in account_list]

class IncidentReportForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	reported_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	incident_type = forms.ChoiceField(choices=[('Safety', 'Safety'), ('Quality', 'Quality')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	immediate_action = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		reported_by_list = kwargs.pop('reported_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['reported_by_id'].choices = [(item['id'], item['first_name']) for item in reported_by_list]

class InspectionForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	inspector_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	inspection_type = forms.ChoiceField(choices=[('Safety', 'Safety'), ('Quality', 'Quality')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	checklist = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	findings = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		inspector_list = kwargs.pop('inspector_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['inspector_id'].choices = [(item['id'], item['first_name']) for item in inspector_list]

class LegalRequirementForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	requirement_type = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class MessageForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	content = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class MilestoneForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	target_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	client_review_required = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class MilestoneBillingForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	milestone_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	due_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	invoiced = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class PayrollForm(forms.Form):
	worker_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	pay_period_start = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	pay_period_end = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	total_hours = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	hourly_rate = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_pay = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		worker_list = kwargs.pop('worker_choice', [])
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['worker_id'].choices = [(item['id'], item['first_name']) for item in worker_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class PostProjectReviewForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	review_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	evaluation_summary = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	strengths = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	areas_for_improvement = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	lessons_learned = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	recommendations = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ProjectCloseoutForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	subcontractor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	final_inspection_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	punch_list_items = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	punch_list_completed = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	final_payment = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		subcontractor_list = kwargs.pop('subcontractor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['subcontractor_id'].choices = [(item['id'], item['name']) for item in subcontractor_list]

class ProjectCommunicationForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	message = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ProjectDocumentationForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	document_type = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	issue_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ProjectFinancialCloseoutForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	closeout_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	total_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_revenue = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_profit = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	subcontractors_paid = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	purchase_orders_closed = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ProjectPerformanceReviewForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	review_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	original_budget = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	actual_budget = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	resource_utilization_percentage = forms.FloatField(required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ProjectScheduleForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	end_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class PunchListItemForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('Pending', 'Pending'), ('In Progress', 'In progress'), ('Completed', 'Completed')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	contractor_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	resolved_at = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	fix_deadline = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	inspected = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	quality_meets_standards = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		contractor_list = kwargs.pop('contractor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['contractor_id'].choices = [(item['id'], item['name']) for item in contractor_list]

class QualityControlPlanForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	content = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class QualityInspectorForm(forms.Form):
	user_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	designation = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		user_list = kwargs.pop('user_choice', [])
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['user_id'].choices = [(item['id'], item['first_name']) for item in user_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ResourcePlanningForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	workforce_required = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	project_duration = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class ResourceUtilizationAnalysisForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	analysis_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	total_labor_hours = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_materials_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_equipment_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	labor_utilization_percentage = forms.FloatField(required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	materials_utilization_percentage = forms.FloatField(required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	equipment_utilization_percentage = forms.FloatField(required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	recommendations = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class RevenueForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	customer_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	received_by = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		customer_list = kwargs.pop('customer_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['customer_id'].choices = [(item['id'], item['name']) for item in customer_list]

class RiskForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	risk_category_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	risk_type = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	date_identified = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	owner_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	status = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		risk_category_list = kwargs.pop('risk_category_choice', [])
		owner_list = kwargs.pop('owner_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['risk_category_id'].choices = [(item['id'], item['name']) for item in risk_category_list]
		self.fields['owner_id'].choices = [(item['id'], item['name']) for item in owner_list]

class SafetyOfficerForm(forms.Form):
	user_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	designation = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		user_list = kwargs.pop('user_choice', [])
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['user_id'].choices = [(item['id'], item['first_name']) for item in user_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class SafetyPlanForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	content = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class SubcontractorContractForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	subcontractor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	signed_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	payment_terms = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	insurance_requirements = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	change_order_provision = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	termination_conditions = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		subcontractor_list = kwargs.pop('subcontractor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['subcontractor_id'].choices = [(item['id'], item['name']) for item in subcontractor_list]

class ResourceAvailabilityForm(forms.Form):
	resource_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	available_from = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	available_until = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		resource_list = kwargs.pop('resource_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['resource_id'].choices = [(item['id'], item['resource_type']) for item in resource_list]

class ClarificationDocumentForm(forms.Form):
	rfp_rfq_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		rfp_rfq_list = kwargs.pop('rfp_rfq_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['rfp_rfq_id'].choices = [(item['id'], item['title']) for item in rfp_rfq_list]

class StakeholderForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	role_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		role_list = kwargs.pop('role_choice', [])
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['role_id'].choices = [(item['id'], item['name']) for item in role_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class TeamMemberForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	role_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	permissions = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		role_list = kwargs.pop('role_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['role_id'].choices = [(item['id'], item['name']) for item in role_list]

class ExpenseForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	account_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	vendor_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	approved_by = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		account_list = kwargs.pop('account_choice', [])
		vendor_list = kwargs.pop('vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['account_id'].choices = [(item['id'], item['name']) for item in account_list]
		self.fields['vendor_id'].choices = [(item['id'], item['name']) for item in vendor_list]

class PrequalificationQuestionnaireForm(forms.Form):
	vendor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project_experience = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	financial_status = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	certifications = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	safety_records = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	other_qualifications = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		vendor_list = kwargs.pop('vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['vendor_id'].choices = [(item['id'], item['name']) for item in vendor_list]

class RFPRFQDistributionForm(forms.Form):
	rfp_rfq_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	vendor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date_sent = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	response_submitted = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	submission_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		rfp_rfq_list = kwargs.pop('rfp_rfq_choice', [])
		vendor_list = kwargs.pop('vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['rfp_rfq_id'].choices = [(item['id'], item['title']) for item in rfp_rfq_list]
		self.fields['vendor_id'].choices = [(item['id'], item['name']) for item in vendor_list]

class SupplierPerformanceEvaluationForm(forms.Form):
	vendor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	evaluation_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	delivery_timeliness = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	quality_of_products_services = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	overall_execution = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	average_score = forms.FloatField(required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		vendor_list = kwargs.pop('vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['vendor_id'].choices = [(item['id'], item['name']) for item in vendor_list]

class VendorClarificationForm(forms.Form):
	rfp_rfq_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	vendor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	question = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		rfp_rfq_list = kwargs.pop('rfp_rfq_choice', [])
		vendor_list = kwargs.pop('vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['rfp_rfq_id'].choices = [(item['id'], item['title']) for item in rfp_rfq_list]
		self.fields['vendor_id'].choices = [(item['id'], item['name']) for item in vendor_list]

class VendorPrequalificationStatusForm(forms.Form):
	vendor_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	prequalified = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	prequalification_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	reasons_for_rejection = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		vendor_list = kwargs.pop('vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['vendor_id'].choices = [(item['id'], item['name']) for item in vendor_list]

class VendorProposalForm(forms.Form):
	rfp_rfq_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	vendor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	is_compliant = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	compliance_remarks = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		rfp_rfq_list = kwargs.pop('rfp_rfq_choice', [])
		vendor_list = kwargs.pop('vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['rfp_rfq_id'].choices = [(item['id'], item['title']) for item in rfp_rfq_list]
		self.fields['vendor_id'].choices = [(item['id'], item['name']) for item in vendor_list]

class AssetAuditForm(forms.Form):
	asset_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	audit_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	condition = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	comments = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		asset_list = kwargs.pop('asset_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['asset_id'].choices = [(item['id'], item['name']) for item in asset_list]

class AssetMaintenanceForm(forms.Form):
	asset_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	maintenance_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	maintenance_type = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	notes = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		asset_list = kwargs.pop('asset_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['asset_id'].choices = [(item['id'], item['name']) for item in asset_list]

class DepreciationForm(forms.Form):
	asset_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	depreciation_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		asset_list = kwargs.pop('asset_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['asset_id'].choices = [(item['id'], item['name']) for item in asset_list]

class SubmissionFollowUpForm(forms.Form):
	proposal_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	submission_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	follow_up_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	follow_up_notes = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	negotiation_engaged = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	revisions_required = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		proposal_list = kwargs.pop('proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['proposal_id'].choices = [(item['id'], item['proposal_title']) for item in proposal_list]

class NegotiationAndAwardForm(forms.Form):
	bid_submission_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	negotiation_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	negotiation_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	final_terms = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	awarded = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	internal_preparation_started = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		bid_submission_list = kwargs.pop('bid_submission_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['bid_submission_id'].choices = [(item['id'], item['submission_date']) for item in bid_submission_list]

class PostSubmissionFollowUpForm(forms.Form):
	bid_submission_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	follow_up_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	communication_method = forms.ChoiceField(choices=[('email', 'Email'), ('phone', 'Phone'), ('meeting', 'Meeting')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	client_response = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	clarification_requested = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	additional_info_provided = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		bid_submission_list = kwargs.pop('bid_submission_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['bid_submission_id'].choices = [(item['id'], item['submission_date']) for item in bid_submission_list]

class EquipmentAssignmentForm(forms.Form):
	equipment_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	assigned_to = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	assigned_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	return_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		equipment_list = kwargs.pop('equipment_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['equipment_id'].choices = [(item['id'], item['name']) for item in equipment_list]

class EquipmentAuditForm(forms.Form):
	equipment_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	audit_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	condition = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		equipment_list = kwargs.pop('equipment_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['equipment_id'].choices = [(item['id'], item['name']) for item in equipment_list]

class EquipmentMaintenanceForm(forms.Form):
	equipment_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	maintenance_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	maintenance_type = forms.ChoiceField(choices=[('Preventive', 'Preventive'), ('Corrective', 'Corrective')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	notes = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		equipment_list = kwargs.pop('equipment_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['equipment_id'].choices = [(item['id'], item['name']) for item in equipment_list]

class InventoryAuditForm(forms.Form):
	item_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	audit_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	physical_count = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	system_count = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	discrepancy = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		item_list = kwargs.pop('item_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['item_id'].choices = [(item['id'], item['name']) for item in item_list]

class RequisitionForm(forms.Form):
	item_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	quantity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	requested_by = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	date_requested = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	date_fulfilled = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		item_list = kwargs.pop('item_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['item_id'].choices = [(item['id'], item['name']) for item in item_list]

class StockEntryForm(forms.Form):
	item_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	quantity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	movement_type = forms.ChoiceField(choices=[('IN', 'In'), ('OUT', 'Out')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		item_list = kwargs.pop('item_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['item_id'].choices = [(item['id'], item['name']) for item in item_list]

class ClientInteractionForm(forms.Form):
	lead_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	interaction_type_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	follow_up_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		lead_list = kwargs.pop('lead_choice', [])
		interaction_type_list = kwargs.pop('interaction_type_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['lead_id'].choices = [(item['id'], item['name']) for item in lead_list]
		self.fields['interaction_type_id'].choices = [(item['id'], item['type_name']) for item in interaction_type_list]

class OpportunityForm(forms.Form):
	lead_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	stage_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	probability = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	expected_close_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	assigned_to_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		lead_list = kwargs.pop('lead_choice', [])
		stage_list = kwargs.pop('stage_choice', [])
		assigned_to_list = kwargs.pop('assigned_to_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['lead_id'].choices = [(item['id'], item['name']) for item in lead_list]
		self.fields['stage_id'].choices = [(item['id'], item['name']) for item in stage_list]
		self.fields['assigned_to_id'].choices = [(item['id'], item['name']) for item in assigned_to_list]

class DocumentedRequirementForm(forms.Form):
	procurement_need_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	requirement_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	requirement_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	timeline = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	budget_estimate = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	technical_specifications = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	quality_specifications = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		procurement_need_list = kwargs.pop('procurement_need_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['procurement_need_id'].choices = [(item['id'], item['description']) for item in procurement_need_list]

class CorrectivePreventiveActionForm(forms.Form):
	audit_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	date_taken = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	status = forms.ChoiceField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		audit_list = kwargs.pop('audit_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['audit_id'].choices = [(item['id'], item['audit_type']) for item in audit_list]

class ChangeOrderForm(forms.Form):
	contract_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	requestor = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	change_reason = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	impact_on_scope = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	cost_impact = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	time_impact = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	status = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	submitted_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	approved_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]

class ContractCloseoutForm(forms.Form):
	contract_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	closeout_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	final_review_notes = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	signed_off_by = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]

class ContractExecutionForm(forms.Form):
	contract_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	execution_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	status = forms.ChoiceField(choices=[('in_progress', 'In_progress'), ('completed', 'Completed'), ('terminated', 'Terminated')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]

class ContractMilestoneForm(forms.Form):
	contract_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	due_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	completed = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]

class LegalReviewForm(forms.Form):
	contract_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	review_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	reviewed_by = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	approval_status = forms.ChoiceField(choices=[('approved', 'Approved'), ('revised', 'Revised'), ('not_approved', 'Not_approved')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]

class PurchaseOrderForm(forms.Form):
	contract_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	order_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	product_service_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	product_service_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	unit_price = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_price = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]

class CorrectiveActionForm(forms.Form):
	incident_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	action_taken_by_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	date_taken = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	status = forms.ChoiceField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		incident_list = kwargs.pop('incident_choice', [])
		action_taken_by_list = kwargs.pop('action_taken_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['incident_id'].choices = [(item['id'], item['incident_type']) for item in incident_list]
		self.fields['action_taken_by_id'].choices = [(item['id'], item['first_name']) for item in action_taken_by_list]

class InvestigationForm(forms.Form):
	incident_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	investigator_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	findings = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	root_cause = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	investigation_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		incident_list = kwargs.pop('incident_choice', [])
		investigator_list = kwargs.pop('investigator_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['incident_id'].choices = [(item['id'], item['incident_type']) for item in incident_list]
		self.fields['investigator_id'].choices = [(item['id'], item['first_name']) for item in investigator_list]

class ClientReviewForm(forms.Form):
	milestone_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	client_feedback = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	approved = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		milestone_list = kwargs.pop('milestone_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['milestone_id'].choices = [(item['id'], item['name']) for item in milestone_list]

class ScheduleAdjustmentForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	milestone_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	adjustment_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	new_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	reason = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	adjusted_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		milestone_list = kwargs.pop('milestone_choice', [])
		adjusted_by_list = kwargs.pop('adjusted_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['milestone_id'].choices = [(item['id'], item['name']) for item in milestone_list]
		self.fields['adjusted_by_id'].choices = [(item['id'], item['first_name']) for item in adjusted_by_list]

class TaskForm(forms.Form):
	milestone_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	is_completed = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	duration_estimation_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	priority_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	category_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	assigned_team_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	assigned_individuals_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	task_owner_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		milestone_list = kwargs.pop('milestone_choice', [])
		duration_estimation_list = kwargs.pop('duration_estimation_choice', [])
		priority_list = kwargs.pop('priority_choice', [])
		category_list = kwargs.pop('category_choice', [])
		assigned_team_list = kwargs.pop('assigned_team_choice', [])
		assigned_individuals_list = kwargs.pop('assigned_individuals_choice', [])
		task_owner_list = kwargs.pop('task_owner_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['milestone_id'].choices = [(item['id'], item['name']) for item in milestone_list]
		self.fields['duration_estimation_id'].choices = [(item['id'], item['pk']) for item in duration_estimation_list]
		self.fields['priority_id'].choices = [(item['id'], item['priority_level']) for item in priority_list]
		self.fields['category_id'].choices = [(item['id'], item['category_name']) for item in category_list]
		self.fields['assigned_team_id'].choices = [(item['id'], item['name']) for item in assigned_team_list]
		self.fields['assigned_individuals_id'].choices = [(item['id'], item['name']) for item in assigned_individuals_list]
		self.fields['task_owner_id'].choices = [(item['id'], item['name']) for item in task_owner_list]

class SiteInspectionForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	inspection_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	inspector_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	observations = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	punch_list_items_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		inspector_list = kwargs.pop('inspector_choice', [])
		punch_list_items_list = kwargs.pop('punch_list_items_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['inspector_id'].choices = [(item['id'], item['first_name']) for item in inspector_list]
		self.fields['punch_list_items_id'].choices = [(item['id'], item['description']) for item in punch_list_items_list]

class MachineryForm(forms.Form):
	resource_planning_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	quantity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		resource_planning_list = kwargs.pop('resource_planning_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['resource_planning_id'].choices = [(item['id'], item['workforce_required']) for item in resource_planning_list]

class MaterialForm(forms.Form):
	resource_planning_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	quantity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		resource_planning_list = kwargs.pop('resource_planning_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['resource_planning_id'].choices = [(item['id'], item['workforce_required']) for item in resource_planning_list]

class MitigationStrategyForm(forms.Form):
	risk_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	strategy = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	mitigation_owner_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	end_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	status = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		risk_list = kwargs.pop('risk_choice', [])
		mitigation_owner_list = kwargs.pop('mitigation_owner_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['risk_id'].choices = [(item['id'], item['name']) for item in risk_list]
		self.fields['mitigation_owner_id'].choices = [(item['id'], item['name']) for item in mitigation_owner_list]

class RiskAssessmentForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	risk_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	probability = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	impact = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	overall_risk_score = forms.FloatField( required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		risk_list = kwargs.pop('risk_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['risk_id'].choices = [(item['id'], item['name']) for item in risk_list]

class RiskReviewForm(forms.Form):
	risk_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	review_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	status = forms.ChoiceField(choices=[('Open', 'Open'), ('Mitigated', 'Mitigated'), ('Closed', 'Closed')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	reviewed_by_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		risk_list = kwargs.pop('risk_choice', [])
		reviewed_by_list = kwargs.pop('reviewed_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['risk_id'].choices = [(item['id'], item['name']) for item in risk_list]
		self.fields['reviewed_by_id'].choices = [(item['id'], item['name']) for item in reviewed_by_list]

class DelayNotificationForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	stakeholder_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	notification_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	message = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	updated_timeline = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	plan_to_mitigate = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		stakeholder_list = kwargs.pop('stakeholder_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['stakeholder_id'].choices = [(item['id'], item['name']) for item in stakeholder_list]

class StakeholderInputForm(forms.Form):
	procurement_need_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	stakeholder_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	input_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		procurement_need_list = kwargs.pop('procurement_need_choice', [])
		stakeholder_list = kwargs.pop('stakeholder_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['procurement_need_id'].choices = [(item['id'], item['description']) for item in procurement_need_list]
		self.fields['stakeholder_id'].choices = [(item['id'], item['name']) for item in stakeholder_list]

class TenderDocumentForm(forms.Form):
	tender_type = forms.ChoiceField(choices=[('RFP', 'Rfp'), ('RFQ', 'Rfq')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	prepared_by_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	issue_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	closing_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		prepared_by_list = kwargs.pop('prepared_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['prepared_by_id'].choices = [(item['id'], item['name']) for item in prepared_by_list]

class IssueForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	issue_type = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	status = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	assigned_to_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		assigned_to_list = kwargs.pop('assigned_to_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['assigned_to_id'].choices = [(item['id'], item['permissions']) for item in assigned_to_list]

class RFPRFQResponseForm(forms.Form):
	distribution_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	response_text = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		distribution_list = kwargs.pop('distribution_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['distribution_id'].choices = [(item['id'], item['date_sent']) for item in distribution_list]

class ClarificationResponseForm(forms.Form):
	clarification_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	response = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		clarification_list = kwargs.pop('clarification_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['clarification_id'].choices = [(item['id'], item['question']) for item in clarification_list]

class FinalVendorSelectionForm(forms.Form):
	vendor_proposal_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	selection_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	justification = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	approved_by = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		vendor_proposal_list = kwargs.pop('vendor_proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['vendor_proposal_id'].choices = [(item['id'], item['submitted_at']) for item in vendor_proposal_list]

class FinancialEvaluationForm(forms.Form):
	proposal_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	quoted_price = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	hidden_costs = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	delivery_schedule_assessment = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	warranties_offered = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	after_sales_service = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		proposal_list = kwargs.pop('proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['proposal_id'].choices = [(item['id'], item['submitted_at']) for item in proposal_list]

class NegotiationStakeholderForm(forms.Form):
	team_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	stakeholder_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	vendor_proposal_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	feedback = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		team_list = kwargs.pop('team_choice', [])
		stakeholder_list = kwargs.pop('stakeholder_choice', [])
		vendor_proposal_list = kwargs.pop('vendor_proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['team_id'].choices = [(item['id'], item['name']) for item in team_list]
		self.fields['stakeholder_id'].choices = [(item['id'], item['name']) for item in stakeholder_list]
		self.fields['vendor_proposal_id'].choices = [(item['id'], item['submitted_at']) for item in vendor_proposal_list]

class NegotiationSummaryForm(forms.Form):
	vendor_proposal_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	summary = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	final_terms_agreed = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		vendor_proposal_list = kwargs.pop('vendor_proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['vendor_proposal_id'].choices = [(item['id'], item['submitted_at']) for item in vendor_proposal_list]

class NegotiationTermForm(forms.Form):
	description = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	proposed_value = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	negotiated_value = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	vendor_proposal_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		vendor_proposal_list = kwargs.pop('vendor_proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['vendor_proposal_id'].choices = [(item['id'], item['submitted_at']) for item in vendor_proposal_list]

class ProposalComplianceForm(forms.Form):
	proposal_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	certification_compliance = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	technical_spec_compliance = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	other_compliance = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		proposal_list = kwargs.pop('proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['proposal_id'].choices = [(item['id'], item['submitted_at']) for item in proposal_list]

class ProposalEvaluationForm(forms.Form):
	proposal_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	total_score = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	shortlisted = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		proposal_list = kwargs.pop('proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['proposal_id'].choices = [(item['id'], item['submitted_at']) for item in proposal_list]

class ProposalScoringForm(forms.Form):
	proposal_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	criteria_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	score = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		proposal_list = kwargs.pop('proposal_choice', [])
		criteria_list = kwargs.pop('criteria_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['proposal_id'].choices = [(item['id'], item['submitted_at']) for item in proposal_list]
		self.fields['criteria_id'].choices = [(item['id'], item['name']) for item in criteria_list]

class RiskEvaluationForm(forms.Form):
	proposal_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	vendor_reliability = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	financial_stability = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	logistical_issues = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	overall_risk_level = forms.ChoiceField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		proposal_list = kwargs.pop('proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['proposal_id'].choices = [(item['id'], item['submitted_at']) for item in proposal_list]

class TechnicalEvaluationForm(forms.Form):
	proposal_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	meets_technical_specs = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	quality_assessment = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	additional_technical_remarks = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		proposal_list = kwargs.pop('proposal_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['proposal_id'].choices = [(item['id'], item['submitted_at']) for item in proposal_list]

class ProposalForm(forms.Form):
	opportunity_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('sent', 'Sent'), ('viewed', 'Viewed'), ('negotiation', 'Negotiation'), ('approved', 'Approved')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	negotiation_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		opportunity_list = kwargs.pop('opportunity_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['opportunity_id'].choices = [(item['id'], item['amount']) for item in opportunity_list]

class AuditLogForm(forms.Form):
	contract_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	change_order_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	action = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	action_by = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		change_order_list = kwargs.pop('change_order_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]
		self.fields['change_order_id'].choices = [(item['id'], item['requestor']) for item in change_order_list]

class ChangeOrderApprovalForm(forms.Form):
	change_order_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	approved_by = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	approval_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		change_order_list = kwargs.pop('change_order_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['change_order_id'].choices = [(item['id'], item['requestor']) for item in change_order_list]

class ChangeOrderImplementationForm(forms.Form):
	change_order_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	implementation_details = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	implementation_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	new_deadline = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		change_order_list = kwargs.pop('change_order_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['change_order_id'].choices = [(item['id'], item['requestor']) for item in change_order_list]

class DocumentForm(forms.Form):
	contract_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	change_order_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	document_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	upload_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		change_order_list = kwargs.pop('change_order_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]
		self.fields['change_order_id'].choices = [(item['id'], item['requestor']) for item in change_order_list]

class InvoiceForm(forms.Form):
	purchase_order_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	vendor_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	invoice_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	invoice_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	total_amount = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	payment_status = forms.ChoiceField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Paid', 'Paid'), ('Rejected', 'Rejected')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		purchase_order_list = kwargs.pop('purchase_order_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['purchase_order_id'].choices = [(item['id'], item['order_number']) for item in purchase_order_list]

class ShipmentForm(forms.Form):
	purchase_order_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	shipment_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		purchase_order_list = kwargs.pop('purchase_order_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['purchase_order_id'].choices = [(item['id'], item['order_number']) for item in purchase_order_list]

class CriticalPathForm(forms.Form):
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	is_on_critical_path = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		project_list = kwargs.pop('project_choice', [])
		task_list = kwargs.pop('task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]

class DailyProgressReportForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	report_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	worker_count = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	machinery_in_use = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	materials_used = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	completion_percentage = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	progress_percentage = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	issues_encountered = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	reported_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		reported_by_list = kwargs.pop('reported_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]
		self.fields['reported_by_id'].choices = [(item['id'], item['first_name']) for item in reported_by_list]

class DelayForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	cause_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	reported_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		cause_list = kwargs.pop('cause_choice', [])
		reported_by_list = kwargs.pop('reported_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]
		self.fields['cause_id'].choices = [(item['id'], item['cause']) for item in cause_list]
		self.fields['reported_by_id'].choices = [(item['id'], item['first_name']) for item in reported_by_list]

class PerformanceReportForm(forms.Form):
	subcontractor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	report_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	tasks_completed = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	issues_encountered = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	safety_compliance = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	def __init__(self, *args, **kwargs):
		subcontractor_list = kwargs.pop('subcontractor_choice', [])
		project_list = kwargs.pop('project_choice', [])
		task_list = kwargs.pop('task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['subcontractor_id'].choices = [(item['id'], item['name']) for item in subcontractor_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]

class PhotoDocumentationForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	geo_tag = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]

class ProjectUpdateForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	planned_start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	actual_start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	planned_end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	actual_end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	progress_percentage = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]

class ResourceAdjustmentForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	resource_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	adjustment_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	new_schedule = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	reason = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		resource_list = kwargs.pop('resource_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]
		self.fields['resource_id'].choices = [(item['id'], item['resource_type']) for item in resource_list]

class ResourceAllocationForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	resource_type = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	allocated_quantity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	allocated_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		allocated_by_list = kwargs.pop('allocated_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]
		self.fields['allocated_by_id'].choices = [(item['id'], item['first_name']) for item in allocated_by_list]

class TaskDependencyForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	dependent_task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		dependent_task_list = kwargs.pop('dependent_task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]
		self.fields['dependent_task_id'].choices = [(item['id'], item['name']) for item in dependent_task_list]

class TaskResourceAllocationForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	resource_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	resource_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		resource_list = kwargs.pop('resource_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]
		self.fields['resource_id'].choices = [(item['id'], item['resource_type']) for item in resource_list]

class TaskScheduleForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	scheduled_start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	scheduled_end_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]

class TaskStatusForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	status = forms.ChoiceField(choices=[('not_started', 'Not_started'), ('in_progress', 'In_progress'), ('completed', 'Completed'), ('on_hold', 'On_hold')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	update_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]

class TimesheetForm(forms.Form):
	worker_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	hours_worked = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	task_id = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class": "form-control"}))
	submitted = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	reviewed = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		worker_list = kwargs.pop('worker_choice', [])
		project_list = kwargs.pop('project_choice', [])
		task_list = kwargs.pop('task_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['worker_id'].choices = [(item['id'], item['first_name']) for item in worker_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]

class TimeTrackingForm(forms.Form):
	task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	user_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	hours_spent = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	hourly_rate = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	total_cost = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_list = kwargs.pop('task_choice', [])
		user_list = kwargs.pop('user_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_id'].choices = [(item['id'], item['name']) for item in task_list]
		self.fields['user_id'].choices = [(item['id'], item['first_name']) for item in user_list]

class StockAdjustmentForm(forms.Form):
	material_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	quantity_adjusted = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	reason = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	adjustment_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		material_list = kwargs.pop('material_choice', [])
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['material_id'].choices = [(item['id'], item['name']) for item in material_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class StockReplenishmentRequestForm(forms.Form):
	material_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	quantity_requested = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	request_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		material_list = kwargs.pop('material_choice', [])
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['material_id'].choices = [(item['id'], item['name']) for item in material_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class MitigationActionForm(forms.Form):
	mitigation_strategy_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	action_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	action_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	due_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	completed = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	completed_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		mitigation_strategy_list = kwargs.pop('mitigation_strategy_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['mitigation_strategy_id'].choices = [(item['id'], item['strategy']) for item in mitigation_strategy_list]

class TenderScopeForm(forms.Form):
	tender_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	scope_description = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	technical_specifications = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	delivery_timeline = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	quality_standards = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		tender_list = kwargs.pop('tender_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['tender_id'].choices = [(item['id'], item['tender_type']) for item in tender_list]

class TenderSubmissionForm(forms.Form):
	tender_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	vendor_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	proposal_details = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	submitted_on = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	cost_estimate = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		tender_list = kwargs.pop('tender_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['tender_id'].choices = [(item['id'], item['tender_type']) for item in tender_list]

class ContractAwardForm(forms.Form):
	contract_id = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	selected_vendor_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	award_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	notification_sent_to_vendor = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	notification_sent_to_bidders = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
	feedback_to_bidders = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		contract_list = kwargs.pop('contract_choice', [])
		selected_vendor_list = kwargs.pop('selected_vendor_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['contract_id'].choices = [(item['id'], item['scope_of_work']) for item in contract_list]
		self.fields['selected_vendor_id'].choices = [(item['id'], item['selection_date']) for item in selected_vendor_list]

class StakeholderEvaluationForm(forms.Form):
	evaluation_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	stakeholder_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	feedback = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		evaluation_list = kwargs.pop('evaluation_choice', [])
		stakeholder_list = kwargs.pop('stakeholder_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['evaluation_id'].choices = [(item['id'], item['total_score']) for item in evaluation_list]
		self.fields['stakeholder_id'].choices = [(item['id'], item['name']) for item in stakeholder_list]

class PaymentForm(forms.Form):
	invoice_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	payment_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	amount_paid = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	payment_method = forms.ChoiceField(choices=[('Bank Transfer', 'Bank transfer'), ('Credit Card', 'Credit card'), ('Cash', 'Cash'), ('Check', 'Check')], required=True, widget=forms.Select(attrs={"class": "form-control"}))
	payment_reference = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
	project_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	milestone = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	payment_due = forms.FloatField( required=True, widget=forms.NumberInput(attrs={"class": "form-control"}))
	status = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		invoice_list = kwargs.pop('invoice_choice', [])
		project_list = kwargs.pop('project_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['invoice_id'].choices = [(item['id'], item['vendor_name']) for item in invoice_list]
		self.fields['project_id'].choices = [(item['id'], item['name']) for item in project_list]

class CriticalPathMonitoringForm(forms.Form):
	critical_path_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	actual_start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	actual_end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	actual_end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		critical_path_list = kwargs.pop('critical_path_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['critical_path_id'].choices = [(item['id'], item['is_on_critical_path']) for item in critical_path_list]

class AdjustmentForm(forms.Form):
	delay_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	adjusted_task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	new_start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	new_end_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	adjusted_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	adjustment_reason = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		delay_list = kwargs.pop('delay_choice', [])
		adjusted_task_list = kwargs.pop('adjusted_task_choice', [])
		adjusted_by_list = kwargs.pop('adjusted_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['delay_id'].choices = [(item['id'], item['reported_at']) for item in delay_list]
		self.fields['adjusted_task_id'].choices = [(item['id'], item['name']) for item in adjusted_task_list]
		self.fields['adjusted_by_id'].choices = [(item['id'], item['first_name']) for item in adjusted_by_list]

class ResourceReallocationForm(forms.Form):
	original_allocation_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	new_task_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	reallocated_quantity = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"class": "form-control"}))
	reason = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
	reallocated_by_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	def __init__(self, *args, **kwargs):
		original_allocation_list = kwargs.pop('original_allocation_choice', [])
		new_task_list = kwargs.pop('new_task_choice', [])
		reallocated_by_list = kwargs.pop('reallocated_by_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['original_allocation_id'].choices = [(item['id'], item['resource_type']) for item in original_allocation_list]
		self.fields['new_task_id'].choices = [(item['id'], item['name']) for item in new_task_list]
		self.fields['reallocated_by_id'].choices = [(item['id'], item['first_name']) for item in reallocated_by_list]

class ResourceUsageForm(forms.Form):
	task_resource_allocation_id = forms.ChoiceField(choices=[],required=True, widget=forms.Select(attrs={"class": "form-control"}))
	start_time = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	end_time = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	end_time = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={"type": "date","class": "form-control"}))
	def __init__(self, *args, **kwargs):
		task_resource_allocation_list = kwargs.pop('task_resource_allocation_choice', [])
		super().__init__(*args, **kwargs)
		self.fields['task_resource_allocation_id'].choices = [(item['id'], item['pk']) for item in task_resource_allocation_list]

class ClientForm(forms.Form):
	name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	address = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	contact_person = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"type": "email","class": "form-control"}))
	phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class BidQualificationForm(forms.Form):
	rfp_rfq_title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	response_due_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	alignment_with_strategy = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	capacity_evaluation = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	is_qualified = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))

class TenderProposalManagementForm(forms.Form):
	rfp_rfq_title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
	issued_date = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	response_deadline = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date","class": "form-control"}))
	response_tracking = forms.CharField( required=True, widget=forms.Textarea(attrs={"class": "form-control"}))
	issued_by = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))


class TaskDurationEstimationForm(forms.Form):
	estimated_duration = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))

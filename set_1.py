def savings(gross_pay, tax_rate, expenses):
  after_tax = int(gross_pay * (1 - tax_rate))
  remaining = after_tax - expenses
  return remaining

def material_waste(total_material, material_ubits, num_jobs, job_consumption):
  total_used = num_jobs * job_consumption
  waste = total_material - total_used
  return f"{waste}{material_units}"

def interest(principal, rate, periods):
  final_value = principal + (principal * rate * periods)
  return int(final_value)
  

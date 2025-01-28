PROMPT = f"""
Leukocytes (leu):
Leukocytes refer to white blood cells present in urine. Their presence typically indicates infection, inflammation, or immune response in the urinary tract.

Normal: 0 leu/μL (no white blood cells detected)
Abnormal: Elevated levels suggest urinary tract infections (UTI) or kidney disease.
Nitrites (nit):
Nitrites are chemical compounds that indicate bacterial activity, as certain bacteria convert nitrates to nitrites.

Normal: Negative (no nitrites detected)
Abnormal: Positive results are a marker of bacterial infection, particularly UTIs.
Urobilinogen (uro):
Urobilinogen is a byproduct of bilirubin metabolism, providing insight into liver function and hemolysis.

Normal: 0.2 mg/dL (small amounts are normal)
Abnormal: Elevated levels suggest liver disease or hemolytic disorders; low levels may indicate bile obstruction.
Protein (pro):
Protein in urine is an indicator of kidney function, as the kidneys normally filter out proteins.

Normal: 0 mg/dL (no protein detected)
Abnormal: Presence of protein (proteinuria) may signal kidney damage, diabetes, or high blood pressure.
pH (ph):
The pH of urine measures its acidity or alkalinity, reflecting diet, metabolic processes, or infections.

Normal: 4.5–8.0 (slightly acidic to slightly alkaline)
Abnormal: Acidic urine may result from high protein intake or acidosis, while alkaline urine can indicate infections or a vegetarian diet.
Blood (blo):
Blood in urine may indicate injury, infection, stones, or other conditions affecting the urinary tract.

Normal: 0 Ery/μL (no blood detected)
Abnormal: Presence of blood (hematuria) requires further investigation for infections, trauma, or malignancies.
Specific Gravity (sg):
Specific gravity measures urine concentration, reflecting hydration levels and kidney function.

Normal: 1.005–1.030 (balanced hydration and solute concentration)
Abnormal: Low SG indicates dilute urine (overhydration), while high SG suggests concentrated urine (dehydration or other conditions).
Ketones (ket):
Ketones are produced during fat metabolism and may signal issues like diabetes, starvation, or excessive exercise.

Normal: 0 mg/dL (no ketones detected)
Abnormal: Elevated levels (ketonuria) may indicate diabetes (especially ketoacidosis), fasting, or malnutrition.
Bilirubin (bil):
Bilirubin is a byproduct of red blood cell breakdown, used to evaluate liver and bile duct function.

Normal: 0 mg/dL (no bilirubin detected)
Abnormal: Presence suggests liver disease or bile duct obstruction.
Glucose (glu):
Glucose in urine indicates blood sugar levels exceeding the renal threshold, often linked to diabetes.

Normal: 0 mg/dL (no glucose detected)
Abnormal: Detected glucose (glucosuria) is common in diabetes or after high sugar intake.

with these parameter definitions, and this being my test result
"""
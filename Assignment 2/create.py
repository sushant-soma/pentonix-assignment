from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()

slide_width = prs.slide_width
slide_height = prs.slide_height

image_width = Inches(4)
image_height = Inches(3)  
text_width = slide_width - image_width
text_height = slide_height

slide1 = prs.slides.add_slide(prs.slide_layouts[5])  

img_path1 = 'slide1.png'  
left_img1 = slide_width - image_width
top_img1 = (slide_height - image_height) / 2  
slide1.shapes.add_picture(img_path1, left_img1, top_img1, image_width, image_height)

left_text1 = 0
top_text1 = 0
text_box1 = slide1.shapes.add_textbox(left_text1, top_text1, text_width, text_height)
text_frame1 = text_box1.text_frame

p1 = text_frame1.add_paragraph()
p1.text = "Presentation Skills"
font1 = p1.runs[0].font
font1.color.rgb = RGBColor(0, 0, 255)
p1.alignment = PP_ALIGN.CENTER  

slide2 = prs.slides.add_slide(prs.slide_layouts[5])  

left_intro = Inches(0.5)  
top_intro = Inches(1.0)  
width_intro = slide_width - Inches(1.0)
height_intro = Inches(2.0)  

text_box2 = slide2.shapes.add_textbox(left_intro, top_intro, width_intro, height_intro)
text_frame2 = text_box2.text_frame

p2 = text_frame2.add_paragraph()
p2.text = "Introduction"
font2 = p2.runs[0].font
font2.size = Pt(36)  
font2.color.rgb = RGBColor(0, 0, 255)  
p2.alignment = PP_ALIGN.CENTER  

img_path2 = 'slide2.png'  
image_width2 = slide_width - Inches(1.0)  
image_height2 = slide_height - top_intro - height_intro - Inches(1)  
left_img2 = Inches(0.5)  
top_img2 = top_intro + height_intro + Inches(0.25)  

slide2.shapes.add_picture(img_path2, left_img2, top_img2, image_width2, image_height2)

slide3 = prs.slides.add_slide(prs.slide_layouts[5])  

left_lo = Inches(0.5)  
top_lo = Inches(1.0)  
width_lo = slide_width - Inches(1.0)
height_lo = Inches(2.0)  

text_box3 = slide3.shapes.add_textbox(left_lo, top_lo, width_lo, height_lo)
text_frame3 = text_box3.text_frame

p3 = text_frame3.add_paragraph()
p3.text = "Learning Objectives"
font3 = p3.runs[0].font
font3.size = Pt(36)  
font3.color.rgb = RGBColor(0, 0, 255)  
p3.alignment = PP_ALIGN.CENTER  

img_path3 = 'slide3.png'  
image_width3 = slide_width - Inches(1.0)  
image_height3 = slide_height - top_lo - height_lo - Inches(1)  
left_img3 = Inches(0.5)  
top_img3 = top_lo + height_lo + Inches(0.25)  

slide3.shapes.add_picture(img_path3, left_img3, top_img3, image_width3, image_height3)

slide4 = prs.slides.add_slide(prs.slide_layouts[5])  

img_path4 = 'slide4.png'  
left_img4 = slide_width - image_width
top_img4 = (slide_height - image_height) / 2  
slide4.shapes.add_picture(img_path4, left_img4, top_img4, image_width, image_height)

left_heading = Inches(0.5)  
top_heading = Inches(1.0)  
width_heading = text_width
height_heading = Inches(1.0)  

text_box_heading = slide4.shapes.add_textbox(left_heading, top_heading, width_heading, height_heading)
text_frame_heading = text_box_heading.text_frame

p_heading = text_frame_heading.add_paragraph()
p_heading.text = "The Four Types of Presentation"
font_heading = p_heading.runs[0].font
font_heading.color.rgb = RGBColor(0, 0, 255)  
font_heading.size = Pt(36)  
p_heading.alignment = PP_ALIGN.LEFT  

left_subheading = left_heading
top_subheading = top_heading + height_heading  
width_subheading = text_width
height_subheading = Inches(1.0)  

text_box_subheading = slide4.shapes.add_textbox(left_subheading, top_subheading, width_subheading, height_subheading)
text_frame_subheading = text_box_subheading.text_frame

p_subheading = text_frame_subheading.add_paragraph()
p_subheading.text = "There are four kinds of presentations: informational, instructional, stimulating, and convincing."
font_subheading = p_subheading.runs[0].font
font_subheading.color.rgb = RGBColor(0, 0, 0)  
font_subheading.size = Pt(24)  
p_subheading.alignment = PP_ALIGN.LEFT  

slide5 = prs.slides.add_slide(prs.slide_layouts[5])  

img_path5 = 'slide5.png'  
left_img5 = slide_width - image_width
top_img5 = (slide_height - image_height) / 2  
slide5.shapes.add_picture(img_path5, left_img5, top_img5, image_width, image_height)

left_about_us = Inches(0.5)  
top_about_us = Inches(1.0)  
width_about_us = text_width
height_about_us = Inches(0.5)  

text_box_about_us = slide5.shapes.add_textbox(left_about_us, top_about_us, width_about_us, height_about_us)
text_frame_about_us = text_box_about_us.text_frame

p_about_us = text_frame_about_us.add_paragraph()
p_about_us.text = "About Us"
font_about_us = p_about_us.runs[0].font
font_about_us.color.rgb = RGBColor(255, 0, 0)  
font_about_us.size = Pt(18)  

left_tech_skills = left_about_us
top_tech_skills = top_about_us + height_about_us  
width_tech_skills = text_width
height_tech_skills = Inches(0.5)  

text_box_tech_skills = slide5.shapes.add_textbox(left_tech_skills, top_tech_skills, width_tech_skills, height_tech_skills)
text_frame_tech_skills = text_box_tech_skills.text_frame

p_tech_skills = text_frame_tech_skills.add_paragraph()
p_tech_skills.text = "Technical Skills"
font_tech_skills = p_tech_skills.runs[0].font
font_tech_skills.color.rgb = RGBColor(0, 0, 255)  
font_tech_skills.size = Pt(18)  

slide6 = prs.slides.add_slide(prs.slide_layouts[5])  

img_path6 = 'slide6.png'  
left_img6 = 0  
top_img6 = (slide_height - image_height) / 2  
slide6.shapes.add_picture(img_path6, left_img6, top_img6, image_width, image_height)

left_assessments = text_width  
top_assessments = Inches(1.0)  
width_assessments = slide_width - text_width
height_assessments = Inches(0.5)  

text_box_assessments = slide6.shapes.add_textbox(left_assessments, top_assessments, width_assessments, height_assessments)
text_frame_assessments = text_box_assessments.text_frame

p_assessments = text_frame_assessments.add_paragraph()
p_assessments.text = "Assessments"
font_assessments = p_assessments.runs[0].font
font_assessments.color.rgb = RGBColor(255, 0, 0)  
font_assessments.size = Pt(16)  

left_cyu = left_assessments
top_cyu = top_assessments + height_assessments  
width_cyu = width_assessments
height_cyu = Inches(0.5)  

text_box_cyu = slide6.shapes.add_textbox(left_cyu, top_cyu, width_cyu, height_cyu)
text_frame_cyu = text_box_cyu.text_frame

p_cyu = text_frame_cyu.add_paragraph()
p_cyu.text = "Check Your Understanding"
font_cyu = p_cyu.runs[0].font
font_cyu.color.rgb = RGBColor(0, 0, 255)  
font_cyu.size = Pt(20)  

left_question = left_cyu
top_question = top_cyu + height_cyu  
width_question = width_cyu
height_question = Inches(2.0)  

text_box_question = slide6.shapes.add_textbox(left_question, top_question, width_question, height_question)
text_frame_question = text_box_question.text_frame

p_question = text_frame_question.add_paragraph()
p_question.text = "Q1. Which of the following is the most important part of using presentation skills?\n" \
                 "A. Planning\n" \
                 "B. Preparation\n" \
                 "C. Visualizing success\n" \
                 "D. Exercise/drinking water beforehand"
font_question = p_question.runs[0].font
font_question.color.rgb = RGBColor(0, 0, 0)  
font_question.size = Pt(16)  

prs.save('presentation.pptx')

slide7 = prs.slides.add_slide(prs.slide_layouts[5])  

left_key_points = Inches(0.5)  
top_key_points = Inches(0.5)  
width_key_points = slide_width - Inches(1.0)
height_key_points = Inches(1.0)  

text_box_key_points = slide7.shapes.add_textbox(left_key_points, top_key_points, width_key_points, height_key_points)
text_frame_key_points = text_box_key_points.text_frame

p_key_points = text_frame_key_points.add_paragraph()
p_key_points.text = "Key points"
font_key_points = p_key_points.runs[0].font
font_key_points.color.rgb = RGBColor(0, 0, 255)  
font_key_points.size = Pt(36)  
p_key_points.alignment = PP_ALIGN.CENTER  

img_path7 = 'slide7.png'  
image_width7 = slide_width - Inches(1.0)  
image_height7 = slide_height - top_key_points - height_key_points - Inches(1)  
left_img7 = Inches(0.5)  
top_img7 = top_key_points + height_key_points + Inches(0.25)  

slide7.shapes.add_picture(img_path7, left_img7, top_img7, image_width7, image_height7)

slide8 = prs.slides.add_slide(prs.slide_layouts[5])  

img_path8 = 'slide8.png'  
left_img8 = slide_width - image_width
top_img8 = (slide_height - image_height) / 2  
slide8.shapes.add_picture(img_path8, left_img8, top_img8, image_width, image_height)

left_references = Inches(0.5)  
top_references = Inches(1.0)  
width_references = slide_width - image_width
height_references = Inches(0.5)  

text_box_references = slide8.shapes.add_textbox(left_references, top_references, width_references, height_references)
text_frame_references = text_box_references.text_frame

p_references = text_frame_references.add_paragraph()
p_references.text = "References"
font_references = p_references.runs[0].font
font_references.color.rgb = RGBColor(255, 0, 0)  
font_references.size = Pt(14)  

left_resources = left_references
top_resources = top_references + height_references  
width_resources = width_references
height_resources = Inches(0.75)  

text_box_resources = slide8.shapes.add_textbox(left_resources, top_resources, width_resources, height_resources)
text_frame_resources = text_box_resources.text_frame

p_resources = text_frame_resources.add_paragraph()
p_resources.text = "Additional Resources"
font_resources = p_resources.runs[0].font
font_resources.color.rgb = RGBColor(0, 0, 255)  
font_resources.size = Pt(18)  

img_path8_logo1 = 'slide8_logo1.png'  
image_width8_logo1 = Inches(1.0)  
image_height8_logo1 = Inches(0.5)  
left_img8_logo1 = left_references
top_img8_logo1 = top_resources + height_resources  
top_references_heading = top_img8_logo1 + image_height8_logo1 + Inches(0.1)  

slide8.shapes.add_picture(img_path8_logo1, left_img8_logo1, top_img8_logo1, image_width8_logo1, image_height8_logo1)

text_box_references_heading = slide8.shapes.add_textbox(left_references, top_references_heading, width_references, height_references)
text_frame_references_heading = text_box_references_heading.text_frame

p_references_heading = text_frame_references_heading.add_paragraph()
p_references_heading.text = "References"
font_references_heading = p_references_heading.runs[0].font
font_references_heading.color.rgb = RGBColor(0, 0, 0)  
font_references_heading.size = Pt(14)  

img_path8_logo2 = 'slide8_logo2.png'  
image_width8_logo2 = Inches(1.0)  
image_height8_logo2 = Inches(0.5)  
left_img8_logo2 = left_references
top_img8_logo2 = top_references_heading + height_references  
top_start_learning_heading = top_img8_logo2 + image_height8_logo2 + Inches(0.1)  

slide8.shapes.add_picture(img_path8_logo2, left_img8_logo2, top_img8_logo2, image_width8_logo2, image_height8_logo2)

text_box_start_learning_heading = slide8.shapes.add_textbox(left_references, top_start_learning_heading, width_references, height_references)
text_frame_start_learning_heading = text_box_start_learning_heading.text_frame

p_start_learning_heading = text_frame_start_learning_heading.add_paragraph()
p_start_learning_heading.text = "Start Learning"
font_start_learning_heading = p_start_learning_heading.runs[0].font
font_start_learning_heading.color.rgb = RGBColor(0, 0, 0)  
font_start_learning_heading.size = Pt(14)  

slide9 = prs.slides.add_slide(prs.slide_layouts[5])  

img_path9 = 'slide9.png'  
left_img9 = slide_width - image_width
top_img9 = (slide_height - image_height) / 2  
slide9.shapes.add_picture(img_path9, left_img9, top_img9, image_width, image_height)

left_feedback = Inches(0.5)  
top_feedback = Inches(1.0)  
width_feedback = slide_width - image_width
height_feedback = Inches(0.5)  

text_box_feedback = slide9.shapes.add_textbox(left_feedback, top_feedback, width_feedback, height_feedback)
text_frame_feedback = text_box_feedback.text_frame

p_feedback = text_frame_feedback.add_paragraph()
p_feedback.text = "Feedback"
font_feedback = p_feedback.runs[0].font
font_feedback.color.rgb = RGBColor(255, 0, 0)  
font_feedback.size = Pt(14)  

left_evaluation = left_feedback
top_evaluation = top_feedback + height_feedback  
width_evaluation = width_feedback
height_evaluation = Inches(0.75)  

text_box_evaluation = slide9.shapes.add_textbox(left_evaluation, top_evaluation, width_evaluation, height_evaluation)
text_frame_evaluation = text_box_evaluation.text_frame

p_evaluation = text_frame_evaluation.add_paragraph()
p_evaluation.text = "Course Evaluation"
font_evaluation = p_evaluation.runs[0].font
font_evaluation.color.rgb = RGBColor(0, 0, 255)  
font_evaluation.size = Pt(18)  

left_feedback_form = left_evaluation
top_feedback_form = top_evaluation + height_evaluation  
width_feedback_form = width_evaluation
height_feedback_form = Inches(0.5)  

text_box_feedback_form = slide9.shapes.add_textbox(left_feedback_form, top_feedback_form, width_feedback_form, height_feedback_form)
text_frame_feedback_form = text_box_feedback_form.text_frame

p_feedback_form = text_frame_feedback_form.add_paragraph()
p_feedback_form.text = "Kindly spare a few moments to fill out the course feedback form."
font_feedback_form = p_feedback_form.runs[0].font
font_feedback_form.color.rgb = RGBColor(0, 0, 0)  
font_feedback_form.size = Pt(14)  

left_button = Inches(0.5)  
top_button = top_feedback_form + height_feedback_form + Inches(0.5)  
width_button = Inches(2.0)  
height_button = Inches(0.5)  

button = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 left_button, top_button, width_button, height_button)
button.fill.solid()
button.fill.fore_color.rgb = RGBColor(0, 51, 102)  
button.text = "Submit"  
button.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)  
button.text_frame.paragraphs[0].font.size = Pt(14)  
button.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER  

prs.save('presentation.pptx')

from punctuator import Punctuator
p = Punctuator('Demo-Europarl-EN.pcl')
output_file = open('output.txt', 'w')
output_file.write('Demo-Europarl_EN.pcl\n\n')
output_file.write(p.punctuate('Uh Now last video we went through the first five steps AGADAP So you just kind of shown here of our uh relative combat power that weve chosen to do a penetration umh how weve laid out our forces arrayed them and uh set our phases and selected our leadership Okay so now we get our battle book page were gonna do our COA statement and sketch and we can drive on with our sketch Alright so heres the page out of the battle book and uh we need to do both our sketch and our statement Now for this Im gonna go ahead and and just start with uh the sketch Now uh we know that were gonna start out in our assembly area Alright so we can go ahead and draw that up here at the top of the page and I wanna alot leave uh quite a bit of room down here to show whats gonna happen for actions on the objective Remember the COA sketch isnt to scale uh Were gonna need uh some kind of minor departure We know thats gonna happen Alright and were gonna leave from the uh assembly area and were gonna move to an ORP right So we gotta put our ORP on here uh and since thats gonna be a movement theres gonna be an axis to get us there Alright and uh thinking through this theres probably some phase line here Alright because were gonna spend phase one in the assembly area phase two moving to the ORP and then phase three is all gonna happen in the ORP so theres probably a phase line here because were gonna act differently at that point')) 
#output_file.write(p.punctuate('this is a test sentence for part 1'))

p3 = Punctuator('INTERSPEECH-T-BRNN.pcl')
output_file.write('\n\nINTERSPEECH-T-BRNN.pcl\n\n')
output_file.write(p3.punctuate('Uh Now last video we went through the first five steps AGADAP So you just kind of shown here of our uh relative combat power that weve chosen to do a penetration umh how weve laid out our forces arrayed them and uh set our phases and selected our leadership Okay so now we get our battle book page were gonna do our COA statement and sketch and we can drive on with our sketch Alright so heres the page out of the battle book and uh we need to do both our sketch and our statement Now for this Im gonna go ahead and and just start with uh the sketch Now uh we know that were gonna start out in our assembly area Alright so we can go ahead and draw that up here at the top of the page and I wanna alot leave uh quite a bit of room down here to show whats gonna happen for actions on the objective Remember the COA sketch isnt to scale uh Were gonna need uh some kind of minor departure We know thats gonna happen Alright and were gonna leave from the uh assembly area and were gonna move to an ORP right So we gotta put our ORP on here uh and since thats gonna be a movement theres gonna be an axis to get us there Alright and uh thinking through this theres probably some phase line here Alright because were gonna spend phase one in the assembly area phase two moving to the ORP and then phase three is all gonna happen in the ORP so theres probably a phase line here because were gonna act differently at that point')) 
#output_file.write(p3.punctuate('this is a test sentence for part 3'))

output_file.close()
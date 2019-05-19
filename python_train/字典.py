renDict ={'P' : 'vm_quickplane_P','Pz' : 'vm_quickplane_Pz','N' : 'vm_quickplane_N',
          'Combined Lighting' : 'vm_quickplane_all_comp','Direct Lighting' : 'vm_quickplane_direct_comp',
          'Indirect Lighting' : 'vm_quickplane_indirect_comp','Combined Emission' : 'vm_quickplane_all_emission',
          'Direct Unshadowed' : 'vm_quickplane_direct_noshadow','Direct Ray Samples' : 'vm_quickplane_direct_samples',
          'Indirect Ray Samples' : 'vm_quickplane_indirect_samples','SSS Single' : 'vm_quickplane_sss',
          'Surface Unlit Base Color' : 'vm_quickplane_basecolor','Surface Unlit Diffuse Color' : 'vm_quickplane_diffcolor',
          'Surface Unlit Specular Color' : 'vm_quickplane_speccolor','Surface Emission Color' : 'vm_quickplane_emitcolor',
          'Surface SSS Color' : 'vm_quickplane_ssscolor','Surface Metallic' : 'vm_quickplane_metallic','Surface Specular Roughness' : 'vm_quickplane_specrough'}


selfInput = "P"
print renDict[selfInput]
# path = '/out/mantra1/' + renDict[selfInput]
# parm = hou.parm(path)
# if renDict.has_key(selfInput) and parm.eval() != 0 :
#     parm.set(1)


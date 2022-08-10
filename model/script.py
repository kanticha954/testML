from azureml.core import Workspace
ws = Workspace.create(name='modelHand',
                      subscription_id='9f9160a5-2597-40af-8cef-a374770e6700',
                      resource_group='handRehab',
                      create_resource_group=True,
                      location='East Asia'
                      )

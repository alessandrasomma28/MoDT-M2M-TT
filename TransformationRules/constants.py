CIM_XML_FILE_PATH = "./MDAModelingLevels/01.CIM/VP_GENERATED_XML/project.xml"
CIM_IMPORTED_CLASSES_FILE_PATH = "./TransformationResults/Classes/imported_cimclasses.csv"
CIM_IMPORTED_RELATIONS_FILE_PATH = "./TransformationResults/Relations/imported_cimrelations.csv"

# Meta Class representing the Physical Twin that the Digital Twin seeks to replicate.
CIM_REAL_TWIN_CLASS_NAME = "RealCity"
#Meta Class abstracting entities in the Physical Twin to be digitally replicated.
PHYSICAL_ENTITY_CLASS_NAME="PhysicalEntity"
#Meta Class abstracting temporal entities in the Physical Twin.
TEMPORAL_ENTITY_CLASS_NAME="TemporalEntity"
#Meta Class abstracting sensor entities in the Physical Twin.
SENSOR_ENTITY_CLASS_NAME="Sensor"
#Meta Class abstracting actuator entities in the Physical Twin.
ACTUATOR_ENTITY_CLASS_NAME="Actuator"

PIM_XML_FILE_PATH = "./MDAModelingLevels/02.PIM/M2MT_GENERATED_XML/pim.xml"
PIM_PROJECT_NAME = "PlaformIndependentModel"
PIM_PROJECT_AUTHOR = "PIMAuthor"
PIM_CLASS_DIAGRAM_NAME = "BolognaMobilityDigitalTwin"
PIM_GENERATED_CLASSES_FILE_PATH = "./TransformationResults/Classes/generated_pimclasses.csv"
PIM_GENERATED_RELATIONS_FILE_PATH = "./TransformationResults/Relations/generated_pimrelations.csv"
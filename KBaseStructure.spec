
/*
@author chenry jmc jjeffryes tgu2 qzhang
*/
module KBaseStructure {
  typedef int bool;

  /*
    Reference to KBase genome
    @id ws KBaseGenomes.Genome KBaseGenomeAnnotations.GenomeAnnotation
  */
  typedef string genome_ref;

  /*
    CDS ID
    @id kb
  */
  typedef string cds_id;

  /*
    Molecule ID
    @id external
  */
  typedef string mol_id;

  /*
    Uniref ID
    @id external
  */
  typedef string uniref_id;

  /*
    Reference to a file handle in shock
    @id handle
  */
  typedef string handle_ref;

  /*
    ProteinData
    mol_id id: ID for the protein
    string sequence: amino acid sequence
    string md5: hash of the amino acid sequence
    uniref_id uniref_id: from uniprot
    genome_ref genome_ref: from a kbase genome
    cds_id cds_id: from a kbase genome

    @optional id uniref_id genome_ref cds_id
  */
  typedef structure {
    mol_id id;
    string sequence;
    string md5;
    uniref_id uniref_id;
    genome_ref genome_ref;
    cds_id cds_id;
  } ProteinData;

  /*
    ExperimentalProteinStructure
    @optional mmcif_handle xml_handle
  */
  typedef structure {
    /*Experimental header*/
    string rcsb_id;
    string name;
    string deposition_date;
    string head;
    string release_date;
    string structure_method;
    float resolution;
    string author;
    list<string> compound;
    list<string> source;

    /*Structure metadata*/
    int num_models;
    int num_chains;
    int num_residues;
    int num_atoms;
    int num_het_atoms;
    int num_water_atoms;
    int num_disordered_atoms;
    int num_disordered_residues;

    /*Protein links*/
    list<ProteinData> proteins;

    /*File links*/
    handle_ref pdb_handle;
    handle_ref mmcif_handle;
    handle_ref xml_handle;
  } ExperimentalProteinStructure;

  /*
    ModelProteinStructure
    @optional
  */
  typedef structure {
    string user_data;
    string name;
    int num_chains;
    int num_residues;
    int num_atoms;

    /*Protein links*/
    ProteinData protein;

    /*File links*/
    handle_ref pdb_handle;
  } ModelProteinStructure;


  /*
    ProteinStructures
    model_structures: a list of references to ModelProteinStructures
    experimental_structures: a list of references to ExperimentalProteinStructures
    total_structures: total count of protein structures
    description: description/remarks
    @optional
  */
  typedef structure {
    list<ModelProteinStructure> model_structures;
    list<ExperimentalProteinStructure> experimental_structures;
    int total_structures;
    string description;
  } ProteinStructures;
};


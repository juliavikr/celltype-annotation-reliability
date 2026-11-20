from celltype_rel.ontology import label, depth, relation

B_CELL = "CL:0000236"
MEMORY_B_CELL = "CL:0000787"
T_CELL = "CL:0000084"


def test_label():
    assert label(B_CELL) == "B cell"


def test_child_is_deeper():
    assert depth(MEMORY_B_CELL) > depth(B_CELL)


def test_relation():
    assert relation(B_CELL, B_CELL) == "exact"
    assert relation(B_CELL, MEMORY_B_CELL) == "compatible"
    assert relation(MEMORY_B_CELL, B_CELL) == "compatible"
    assert relation(B_CELL, T_CELL) == "conflict"

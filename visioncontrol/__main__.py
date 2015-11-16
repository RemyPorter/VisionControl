import sys

if sys.argv[1] == "build":
    import build_recognizers
    build_recognizers.descriptions()
    descriptors = build_recognizers.load_descriptors()
    print "Built %i descriptors." % len(descriptors)
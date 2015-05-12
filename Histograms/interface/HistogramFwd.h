#ifndef PLOTS_TOOLS_PLOTFWD
#define PLOTS_TOOLS_PLOTFWD

#include "HEPFWCommon/Histograms/interface/HistogramCollection.h"

// ROOT Includes
#include "TH1F.h"
#include "TH1D.h"
#include "TH2F.h"
#include "TH2D.h"

// C++ Included
#include <map>
#include <string>
#include <utility>

typedef hepfw::HistogramCollection<int,TH1I> hepfw::Map_int_H1I;
typedef hepfw::HistogramCollection<int,TH1F> hepfw::Map_int_H1F;
typedef hepfw::HistogramCollection<int,TH1D> hepfw::Map_int_H1D;
typedef hepfw::HistogramCollection<int,TH2F> hepfw::Map_int_H2F;
typedef hepfw::HistogramCollection<int,TH2D> hepfw::Map_int_H2D;

typedef hepfw::HistogramCollection<std::string,TH1I> hepfw::Map_string_H1I;
typedef hepfw::HistogramCollection<std::string,TH1F> hepfw::Map_string_H1F;
typedef hepfw::HistogramCollection<std::string,TH1D> hepfw::Map_string_H1D;
typedef hepfw::HistogramCollection<std::string,TH2F> hepfw::Map_string_H2F;
typedef hepfw::HistogramCollection<std::string,TH2D> hepfw::Map_string_H2D;

#endif
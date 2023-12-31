import ProblemElement from "../Components/ProblemElement";
import Tag from "../Components/Tag";
import TablePanel from "../Components/TablePanel";
import ContentPanel from "../Components/ContentPanel";
import SearchBar from "../Components/SearchFilters/SearchBar";
import Dropdown from "../Components/SearchFilters/Dropdown";
import { examplePastContests } from "./Contests";
import { tags } from "../public/PublicData";
import RangeSlider from "../Components/SearchFilters/RangeSlider";
import Heading from "../Components/Heading";
import DateInput from "../Components/SearchFilters/DateInput";
import DateRangePicker from "../Components/SearchFilters/DateRangePicker";

export default function Problems() {
  const testTags1 = [
    <Tag key="tag-1">Trigonometry</Tag>,
    <Tag key="tag-2">Geometry</Tag>,
  ];

  const testTags2 = [
    <Tag key="tag-1">Algebra</Tag>,
    <Tag key="tag-2">Linear systems</Tag>,
  ];

  const exampleProblem1 = {
    id: "Q354A",
    name: "Perimeter of a Cat's Head",
    tags: testTags1,
    competitiveRating: 4,
    completedSubmissons: 136,
  };

  const exampleProblem2 = {
    id: "MCSM3",
    name: "Special Pythagorean Triplet",
    tags: testTags2,
    competitiveRating: 2,
    completedSubmissons: 434,
  };

  const exampleProblem3 = {
    id: "IDKXD1",
    name: "Problem",
    tags: testTags1,
    competitiveRating: 1,
    completedSubmissons: 23,
  };

  const problems = [exampleProblem1, exampleProblem2, exampleProblem3];

  const problemNames = problems.map(problem => problem.name);

  const heading = (
    <tr>
      <th title="Problem ID" className="px-3 text-left xl:w-[15%]">
        #
      </th>
      <th title="Problem Name" className="px-3 text-left xl:w-[50%]">
        Problem Name
      </th>
      <th title="Tags" className="px-3 text-left xl:w-[25%]">
        Tags
      </th>
      <th title="Competitive Rating" className="px-3 text-left xl:w-[5%]">
        CR
      </th>
      <th title="Completed Submissions" className="px-3 text-left xl:w-[5%]">
        <img src="../../images/People Icon White.png" className="w-5 h-5"/>
      </th>
    </tr>
  );

  const content = problems.map((problem, index) => (
    <ProblemElement
      key={index}
      problemID={problem.id}
      problemName={problem.name}
      tags={problem.tags}
      competitiveRating={problem.competitiveRating}
      completedSubmissions={problem.completedSubmissons}
    />
  ));

  return (
    <div className="xl:flex flex-row justify-between gap-12 p-6">

      {/*Side content*/}
      <div className="space-y-8 order-1 xl:w-1/4">
        <ContentPanel title="Search Filters">
          <SearchBar hintText="Enter problem name..."/>
          <Dropdown
            label="Origin (Contest Name)"
            options={problemNames}
          />
          <Dropdown
            label="Tags"
            options={tags}
          />
          <RangeSlider
            label="Rating Range"
            min={1}
            max={5}
          />
        </ContentPanel>
      </div>

      {/*Main content*/}
      <div className="xl:w-3/4 mt-8 xl:mt-0">
        <Heading>Problems</Heading>
        <TablePanel heading={heading} content={content} />
      </div>
    </div>
  )
}

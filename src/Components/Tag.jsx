import PropTypes from "prop-types";

export default function Tag({ children }) {
    return <li className="bg-blue-200 p-1 text-xs rounded-md">{children}</li>;
}

Tag.propTypes = {
    children: PropTypes.node,
};
